from antlr4 import *
from SqlVisitor import SqlVisitor
from SqlParser import SqlParser

class SqlExecution(SqlVisitor):
    def __init__(self):
        self.tables = {}
        self.columns = {}
        self.data = {}
        
    def visitProg(self, ctx:SqlParser.ProgContext):
        return self.visit(ctx.expr()) # Just visit the self expression

    def visitCreate_stmt(self, ctx:SqlParser.Create_stmtContext):
        table_name=str(ctx.ID())
        if ctx.ID() in self.tables:
            raise ValueError(f"table {ctx.ID()} already exists")
        else:
            self.tables[ctx.ID()]=table_name
            self.columns[table_name]=[]
            self.data[table_name]=[]
        return self.visitChildren(ctx)

    def visitColumn_spec(self, ctx:SqlParser.Column_specContext):
        table_name=str(ctx.parentCtx.parentCtx.ID())
        column_name=str(ctx.ID())
        column_data=[column_name,ctx.column_type().getText()]
        self.columns[table_name].append(column_data)
        return self.visitChildren(ctx)

    def visitInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        table_name=str(ctx.ID())
        if not table_name in self.columns:
            raise ValueError(f"Table {table_name} is not found")
        val=ctx.VAL()
        count=len(val)
        if count != len(self.columns[table_name]):
            raise ValueError(f"Column count and data count mismatch in table {table_name}")
        else:
            ls=[]
            for i in range(count):
                data_element=val[i].getText()
                data_seg=self.check_data_type(table_name,i,data_element)
                ls.append(data_seg)
                        
        self.data[table_name].append(ls)
        return self.visitChildren(ctx)    
    
    def visitSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        table_name=ctx.ID().getText()
        rows_required=list(range(len(self.data[table_name])))
        if len(ctx.cond())>0:
            selected_rows_list=self.visitConditions(ctx.cond(), table_name, rows_required)
            logical_operators=ctx.LOP()
            combined_list=selected_rows_list[0]
            for i,logical_operator in enumerate(logical_operators):
                combined_list=self.apply_logical_operator(logical_operator.getText(),selected_rows_list[i+1],combined_list)
            rows_required=combined_list
        if ctx.min_max():
            min_max=ctx.min_max()
            type=min_max.MINMAX().getText()
            column_name=min_max.ID().getText()
            column_required=[idx for idx in range(len(self.columns[table_name])) if self.columns[table_name][idx][0]==column_name][0]
            value=self.get_min_max_count(table_name, column_required,rows_required,type)
            print(value)
            print()


        else:
            id_s=ctx.ids()
            ids=id_s.ID()
            
            if not table_name in self.tables.values():
                raise ValueError(f"Table {table_name} not present")
            total_number_of_columns=len(self.columns[table_name])
            all_columns=list(range(total_number_of_columns))
            columns_required=[]
            if ctx.getChild(1).getText()=='*':
                columns_required=all_columns
            else:
                check_list_of_columns=all_columns
                for i in range(len(ids)-1):
                    column_name=ids[i].getText()
                    for j in check_list_of_columns:
                        if column_name==self.columns[table_name][j][0]:
                            columns_required.append(j)
                            check_list_of_columns.remove(j)

            data=self.fetch(table_name, columns_required, rows_required)
            self.show(data)
        

        return self.visitChildren(ctx)
    
    def get_min_max_count(self, table_name, column_required, rows_required, type):
        column_data=self.fetch_column(table_name,column_required,rows_required)
        if type=='MAX':
            column_data.sort()
            return column_data[-1]
        elif type=='MIN':
            column_data.sort()
            return column_data[0]
        elif type=='COUNT':
            return len(column_data)

    def visitDelete_stmt(self, ctx:SqlParser.Delete_stmtContext):
        id=ctx.ID()
        table_name=id.getText()
        if not table_name in self.tables.values():
            raise ValueError(f"Table {table_name} not present")
        total_number_of_columns=len(self.columns[table_name])
        all_columns=list(range(total_number_of_columns))
        rows_required=list(range(len(self.data[table_name])))
        if len(ctx.cond())>0:
            selected_rows_list=self.visitConditions(ctx.cond(), table_name, rows_required)
            logical_operators=ctx.LOP()
            combined_list=selected_rows_list[0]
            for i,logical_operator in enumerate(logical_operators):
                combined_list=self.apply_logical_operator(logical_operator.getText(),selected_rows_list[i+1],combined_list)
            rows_required=combined_list


        self.delete(table_name, rows_required)

        return self.visitChildren(ctx)

    def visitConditions(self, condContextList, table_name, rows_required):
        selected_rows_list=[]
        for ctx in condContextList:
            column_name=ctx.ID().getText()
            operator=ctx.OP().getText()
            value=ctx.VAL().getText()
            column_index=self.check_column_index(table_name,column_name)
            value=self.check_data_type(table_name,column_index,value)
            selected_rows=[]
            for i in rows_required:
                to_check=self.data[table_name][i][column_index]
                flag=self.check_operator(operator,to_check,value)
                if flag:
                    selected_rows.append(i)
            selected_rows_list.append(selected_rows)
        return selected_rows_list

    def visitCond(self, ctx:SqlParser.CondContext):
        return self.visitChildren(ctx)

    def delete(self,table_name,rows_required):
        self.data[table_name]=[row for id, row in enumerate(self.data[table_name]) if id not in rows_required]

    def fetch_column(self, table_name, column_required, rows_required):
        data=[self.data[table_name][i][column_required] for i in rows_required]
        return data

    def fetch(self, table_name, columns_required, rows_required):
        column_names=[self.columns[table_name][j][0] for j in columns_required]
        data=[[self.data[table_name][i][j] for j in columns_required] for i in rows_required]
        data.insert(0,column_names)
        return data

    def show(self, data):
        print()
        spaces=[]
        space=0
        for j in range(len(data[0])):
            for i in range(len(data)):
                space_check=len(str(data[i][j]))
                if space_check>space:
                    space=space_check
            spaces.append(space+3)
            space=0

        for data_row in data:
            for (j,data_element) in enumerate(data_row):
                l=len(str(data_element))
                print(data_element,' '*(spaces[j]-l), end="", flush=True)               
            print()
        print()

    def check_column_index(self,table_name,column_name):
        for i,column_data in enumerate(self.columns[table_name]):
            if column_data[0]==column_name:
                return i

    def check_data_type(self,table_name,column_index,data):
        if self.columns[table_name][column_index][1]=='string':
            if data[0]!='"':
                raise ValueError(f"Column {self.columns[table_name][column_index][1]} of Table {table_name} requires string data type")
            else:
                return data[1:-1]
        else:
            if data[0]=='"':
                raise ValueError(f"Column {self.columns[table_name][column_index][1]} of Table {table_name} requires string int type")
            else:
                return int(data)

    def check_operator(self,operator,to_check,check_with):
        if operator=='=':
            if to_check == check_with:
                return True
            else:
                return False
        elif operator=='>':
            if to_check > check_with:
                return True
            else:
                return False
        elif operator=='<':
            if to_check < check_with:
                return True
            else:
                return False
        elif operator=='>=':
            if to_check >= check_with:
                return True
            else:
                return False
        elif operator=='<=':
            if to_check <= check_with:
                return True
            else:
                return False
        elif operator=='!=':
            if to_check != check_with:
                return True
            else:
                return False

    def apply_logical_operator(self,operator,list1,list2):
        set1=set(list1)
        set2=set(list2)
        if operator=='OR':
            set3=set1.union(set2)
        elif operator=='AND':
            set3=set1.intersection(set2)
        output=list(set3)
        output.sort()
        return output
