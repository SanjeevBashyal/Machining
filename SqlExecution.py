from antlr4 import *
import math as m
from SqlVisitor import SqlVisitor
from SqlParser import SqlParser

class SqlExecution(SqlVisitor):
    def __init__(self,cnc):
        self.cnc=cnc
        self.mode=0
        self.gcode_passive = [21,28,90,91]
        self.current_tip_position = [0,0,0]
        self.last_gcode = None
        self.length_unit = 0 # 0 for millimeters
        self.time = 0
        
    def visitProg(self, ctx:SqlParser.ProgContext):
        return self.visit(ctx.expr()) # Just visit the self expression

    def visitStmt(self, ctx:SqlParser.StmtContext):
        return self.visitChildren(ctx)

    def visitGstmt(self, ctx:SqlParser.GstmtContext):
        GIDs=ctx.GID()
        if len(GIDs)>0:
            for GID in GIDs:
                gcode=GID.getText()
                gcode_type=int(gcode[1:])
                if gcode_type in self.gcode_passive:
                    pass
                else:
                    self.analyze_gsmt(gcode_type,ctx.PID())
        else:
            gcode_type=self.last_gcode
            self.analyze_gsmt(gcode_type,ctx.PID())

        return self.visitChildren(ctx)
    
    def execute_passive_gcodes(self, gcode_type):
        if gcode_type==21:
            self.length_unit=0
        else:
            print(gcode_type,' Not defined')

    def analyze_gsmt(self, gcode_type, PIDs):
        p1=self.current_tip_position
        p2,center=self.analyze_PIDs(PIDs)
        p2=self.analyze_points(p1,p2)
        if gcode_type==0:
            self.run_gcode0(p1,p2)
        elif gcode_type==1:
            self.run_gcode1(p1,p2)
        elif gcode_type==2:
            center=self.analyze_center(p1,center)
            self.run_gcode2(p1,p2,center)
        elif gcode_type==3:
            center=self.analyze_center(p1,center)
            self.run_gcode3(p1,p2,center)
        else:
            print("New G-code found:",gcode_type)
        self.last_gcode=gcode_type

    def run_gcode0(self,p1,p2):
        lc=self.give_max_length(p1,p2)
        T=lc/(self.cnc.axis_maxspeed_rapid_positioning) * 60
        self.time=self.time+T

    def run_gcode1(self,p1,p2):
        lc=self.give_length_straight(p1,p2)
        self.calculate_time_of_exection(lc)

    def run_gcode2(self,p1,p2,c):
        lc=self.give_length_arc_circle(p1,p2,c,1)
        self.calculate_time_of_exection(lc)
        pass

    def run_gcode3(self,p1,p2,c):
        lc=self.give_length_arc_circle(p1,p2,c,0)
        self.calculate_time_of_exection(lc)
        pass

    def calculate_time_of_exection(self, lc):
        T=lc/(self.cnc.current_feed*self.cnc.spindle_rpm) * 60
        self.time=self.time+T

    def analyze_points(self, p1, p2):
        if self.mode:
            for i,val in enumerate(p2):
                if val is None:
                    p2[i]=p1[i]
                else:
                    p2[i]=p1[i]+p2[i]
        else:
            for i,val in enumerate(p2):
                if val is None:
                    p2[i]=p1[i]
        return p2
            
    def analyze_center(self, p1, center):
        for i,val in enumerate(center):
            if val is None:
                center[i]=p1[i]
            else:
                center[i]=p1[i]+center[i]
        return center


    def analyze_PIDs(self, PIDs):
        pos=[None,None,None]
        center=[None,None,None]
        type=self.mode
        for PID in PIDs:
            pcode=PID.getText()
            if pcode[0]=='X':
                pos[0]=float(pcode[1:])
            elif pcode[0]=='Y':
                pos[1]=float(pcode[1:])
            elif pcode[0]=='Z':
                pos[2]=float(pcode[1:])
            if pcode[0]=='I':
                center[0]=float(pcode[1:])
            elif pcode[0]=='J':
                center[1]=float(pcode[1:])
            elif pcode[0]=='K':
                center[2]=float(pcode[1:])
                print("K value defined")
            elif pcode[0]=='F':
                self.cnc.current_feed=float(pcode[1:])
            elif pcode[0]=='S':
                self.cnc.spindle_rpm=float(pcode[1:])
        return (pos,center)

    def give_max_length(self, p1, p2):
        x1,y1,z1=p1
        x2,y2,z2=p2
        x_diff=abs(x2-x1)
        y_diff=abs(y2-y1)
        z_diff=abs(z2-z1)
        if x_diff>y_diff and x_diff>z_diff:
            return x_diff
        elif y_diff>x_diff and y_diff>z_diff:
            return y_diff
        else:
            return z_diff


    def give_length_straight(self,p1,p2):
        x1,y1,z1=p1
        x2,y2,z2=p2
        lc=m.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
        return lc

    def give_length_arc_circle(self,p1,p2,c, clockwise_flag):
        theta=self.give_arc_angle(p1,p2,c,clockwise_flag)
        x1,y1,z1=p1
        x2,y2,z2=p2
        x3,y3,z3=c
        r_sqr_1=(x1-x3)**2+(y1-y3)**2+(z1-z3)**2
        r_sqr_2=(x2-x3)**2+(y2-y3)**2+(z2-z3)**2
        if abs(r_sqr_1-r_sqr_2)<0.01:
            r_sqr=r_sqr_1
        else:
            r_sqr=(r_sqr_1+r_sqr_2)/2
            print("Radius not being same")
        r=m.sqrt(r_sqr)
        lc=r*theta
        return lc

    def give_arc_angle(self,p1,p2,c,clockwise_flag):
        x1,y1,z1=p1
        x2,y2,z2=p2
        x3,y3,z3=c
        theta_1=self.atan2_anticlock(y1-y3,x1-x3)
        theta_2=self.atan2_anticlock(y2-y3,x2-x3)
        theta=theta_2-theta_1
        if clockwise_flag:
            theta=2*m.pi-theta
        return theta

    def atan2_anticlock(self,del_y,del_x):
        theta=m.atan2(del_y,del_x)
        if theta<0:
            theta=theta+2*m.pi
        return theta

    

    # def visitCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
    #     table_name=str(ctx.ID())
    #     if ctx.ID() in self.tables:
    #         raise ValueError(f"table {ctx.ID()} already exists")
    #     else:
    #         self.tables[ctx.ID()]=table_name
    #         self.columns[table_name]=[]
    #         self.data[table_name]=[]
    #     return self.visitChildren(ctx)

    # def visitColumn_spec(self, ctx:SqlParser.Column_specContext):
    #     table_name=str(ctx.parentCtx.parentCtx.ID())
    #     column_name=str(ctx.ID())
    #     column_data=[column_name,ctx.column_type().getText()]
    #     self.columns[table_name].append(column_data)
    #     return self.visitChildren(ctx)

    # def visitInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
    #     table_name=str(ctx.ID())
    #     if not table_name in self.columns:
    #         raise ValueError(f"Table {table_name} is not found")
    #     val=ctx.VAL()
    #     count=len(val)
    #     if count != len(self.columns[table_name]):
    #         raise ValueError(f"Column count and data count mismatch in table {table_name}")
    #     else:
    #         ls=[]
    #         for i in range(count):
    #             data_element=val[i].getText()
    #             data_seg=self.check_data_type(table_name,i,data_element)
    #             ls.append(data_seg)
                        
    #     self.data[table_name].append(ls)
    #     return self.visitChildren(ctx)    
    
    # def visitSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
    #     table_name=ctx.ID().getText()
    #     rows_required=list(range(len(self.data[table_name])))
    #     if len(ctx.cond())>0:
    #         selected_rows_list=self.visitConditions(ctx.cond(), table_name, rows_required)
    #         logical_operators=ctx.LOP()
    #         combined_list=selected_rows_list[0]
    #         for i,logical_operator in enumerate(logical_operators):
    #             combined_list=self.apply_logical_operator(logical_operator.getText(),selected_rows_list[i+1],combined_list)
    #         rows_required=combined_list
    #     if ctx.min_max():
    #         min_max=ctx.min_max()
    #         type=min_max.MINMAX().getText()
    #         column_name=min_max.ID().getText()
    #         column_required=[idx for idx in range(len(self.columns[table_name])) if self.columns[table_name][idx][0]==column_name][0]
    #         value=self.get_min_max_count(table_name, column_required,rows_required,type)
    #         print(value)
    #         print()


    #     else:
    #         id_s=ctx.ids()
    #         ids=id_s.ID()
            
    #         if not table_name in self.tables.values():
    #             raise ValueError(f"Table {table_name} not present")
    #         total_number_of_columns=len(self.columns[table_name])
    #         all_columns=list(range(total_number_of_columns))
    #         columns_required=[]
    #         if ctx.getChild(1).getText()=='*':
    #             columns_required=all_columns
    #         else:
    #             check_list_of_columns=all_columns
    #             for i in range(len(ids)-1):
    #                 column_name=ids[i].getText()
    #                 for j in check_list_of_columns:
    #                     if column_name==self.columns[table_name][j][0]:
    #                         columns_required.append(j)
    #                         check_list_of_columns.remove(j)

    #         data=self.fetch(table_name, columns_required, rows_required)
    #         self.show(data)
        

    #     return self.visitChildren(ctx)
    
    # def get_min_max_count(self, table_name, column_required, rows_required, type):
    #     column_data=self.fetch_column(table_name,column_required,rows_required)
    #     if type=='MAX':
    #         column_data.sort()
    #         return column_data[-1]
    #     elif type=='MIN':
    #         column_data.sort()
    #         return column_data[0]
    #     elif type=='COUNT':
    #         return len(column_data)

    # def visitDelete_stmt(self, ctx:SqlParser.Delete_stmtContext):
    #     id=ctx.ID()
    #     table_name=id.getText()
    #     if not table_name in self.tables.values():
    #         raise ValueError(f"Table {table_name} not present")
    #     total_number_of_columns=len(self.columns[table_name])
    #     all_columns=list(range(total_number_of_columns))
    #     rows_required=list(range(len(self.data[table_name])))
    #     if len(ctx.cond())>0:
    #         selected_rows_list=self.visitConditions(ctx.cond(), table_name, rows_required)
    #         logical_operators=ctx.LOP()
    #         combined_list=selected_rows_list[0]
    #         for i,logical_operator in enumerate(logical_operators):
    #             combined_list=self.apply_logical_operator(logical_operator.getText(),selected_rows_list[i+1],combined_list)
    #         rows_required=combined_list


    #     self.delete(table_name, rows_required)

    #     return self.visitChildren(ctx)

    # def visitConditions(self, condContextList, table_name, rows_required):
    #     selected_rows_list=[]
    #     for ctx in condContextList:
    #         column_name=ctx.ID().getText()
    #         operator=ctx.OP().getText()
    #         value=ctx.VAL().getText()
    #         column_index=self.check_column_index(table_name,column_name)
    #         value=self.check_data_type(table_name,column_index,value)
    #         selected_rows=[]
    #         for i in rows_required:
    #             to_check=self.data[table_name][i][column_index]
    #             flag=self.check_operator(operator,to_check,value)
    #             if flag:
    #                 selected_rows.append(i)
    #         selected_rows_list.append(selected_rows)
    #     return selected_rows_list

    # def visitCond(self, ctx:SqlParser.CondContext):
    #     return self.visitChildren(ctx)

    # def delete(self,table_name,rows_required):
    #     self.data[table_name]=[row for id, row in enumerate(self.data[table_name]) if id not in rows_required]

    # def fetch_column(self, table_name, column_required, rows_required):
    #     data=[self.data[table_name][i][column_required] for i in rows_required]
    #     return data

    # def fetch(self, table_name, columns_required, rows_required):
    #     column_names=[self.columns[table_name][j][0] for j in columns_required]
    #     data=[[self.data[table_name][i][j] for j in columns_required] for i in rows_required]
    #     data.insert(0,column_names)
    #     return data

    # def show(self, data):
    #     print()
    #     spaces=[]
    #     space=0
    #     for j in range(len(data[0])):
    #         for i in range(len(data)):
    #             space_check=len(str(data[i][j]))
    #             if space_check>space:
    #                 space=space_check
    #         spaces.append(space+3)
    #         space=0

    #     for data_row in data:
    #         for (j,data_element) in enumerate(data_row):
    #             l=len(str(data_element))
    #             print(data_element,' '*(spaces[j]-l), end="", flush=True)               
    #         print()
    #     print()

    # def check_column_index(self,table_name,column_name):
    #     for i,column_data in enumerate(self.columns[table_name]):
    #         if column_data[0]==column_name:
    #             return i

    # def check_data_type(self,table_name,column_index,data):
    #     if self.columns[table_name][column_index][1]=='string':
    #         if data[0]!='"':
    #             raise ValueError(f"Column {self.columns[table_name][column_index][1]} of Table {table_name} requires string data type")
    #         else:
    #             return data[1:-1]
    #     else:
    #         if data[0]=='"':
    #             raise ValueError(f"Column {self.columns[table_name][column_index][1]} of Table {table_name} requires string int type")
    #         else:
    #             return int(data)

    # def check_operator(self,operator,to_check,check_with):
    #     if operator=='=':
    #         if to_check == check_with:
    #             return True
    #         else:
    #             return False
    #     elif operator=='>':
    #         if to_check > check_with:
    #             return True
    #         else:
    #             return False
    #     elif operator=='<':
    #         if to_check < check_with:
    #             return True
    #         else:
    #             return False
    #     elif operator=='>=':
    #         if to_check >= check_with:
    #             return True
    #         else:
    #             return False
    #     elif operator=='<=':
    #         if to_check <= check_with:
    #             return True
    #         else:
    #             return False
    #     elif operator=='!=':
    #         if to_check != check_with:
    #             return True
    #         else:
    #             return False

    # def apply_logical_operator(self,operator,list1,list2):
    #     set1=set(list1)
    #     set2=set(list2)
    #     if operator=='OR':
    #         set3=set1.union(set2)
    #     elif operator=='AND':
    #         set3=set1.intersection(set2)
    #     output=list(set3)
    #     output.sort()
    #     return output
