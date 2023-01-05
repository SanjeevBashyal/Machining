from antlr4 import *
import math as m
from GcodeVisitor import GcodeVisitor
from GcodeParser import GcodeParser

class GcodeExecution(GcodeVisitor):
    def __init__(self,cnc):
        self.cnc=cnc
        self.mode=0 # 0 for absolute 1 for relative positioning
        self.gcode_active=[0,1,2,3]
        self.gcode_passive = [28,54,98,40,80,49]
        self.current_tip_position = [0,0,0]
        self.last_gcode = None
        self.length_unit = 0 # 0 for millimeters
        self.time = 0
        self.code_line=0
        
    def visitProg(self, ctx:GcodeParser.ProgContext):
        return self.visit(ctx.expr()) # Just visit the self expression

    def visitStmt(self, ctx:GcodeParser.StmtContext):
        self.code_line=self.code_line+1
        # if self.code_line>364:
        #     print('Here')
        return self.visitChildren(ctx)

    def visitGstmt(self, ctx:GcodeParser.GstmtContext):
        GIDs=ctx.GID()
        if len(GIDs)>0:
            for GID in GIDs:
                gcode=GID.getText()
                code_type=gcode[0]
                if code_type=="G":
                    gcode_type=int(gcode[1:])
                    if gcode_type in self.gcode_active:
                        self.analyze_gsmt(gcode_type,ctx.PID())
                    else:
                        self.execute_passive_gcodes(gcode_type)
                else:
                    self.execute_non_gcodes(gcode)
        else:
            gcode_type=self.last_gcode
            self.analyze_gsmt(gcode_type,ctx.PID())

        return self.visitChildren(ctx)

    def execute_non_gcodes(self, code):
        code_type=code[0]
        if code=='M30':
            print('The execution completed with time T=',self.time)
        if code_type=='T':
            self.time=self.time+self.cnc.tool_change_time
        if code_type=='M6':
            pass #tool change already addressed in instruction T
        else:
            print('New code found:',code)
    
    def execute_passive_gcodes(self, gcode_type):
        if gcode_type==21:
            self.length_unit=0 # 0 for millimeters
        elif gcode_type==90:
            self.mode=0 # 0 for absolute
        elif gcode_type==91:
            self.mode=1 # 1 for relative
        elif gcode_type in self.gcode_passive:
            pass
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
        self.last_gcode=gcode_type

    def run_gcode0(self,p1,p2):
        lc=self.give_max_length(p1,p2)
        T=lc/(self.cnc.axis_maxspeed_rapid_positioning) * 60
        self.time=self.time+T
        self.current_tip_position=p2

    def run_gcode1(self,p1,p2):
        lc=self.give_length_straight(p1,p2)
        self.calculate_time_of_exection(lc)
        self.current_tip_position=p2

    def run_gcode2(self,p1,p2,c):
        lc=self.give_length_arc_circle(p1,p2,c,1)
        self.calculate_time_of_exection(lc)
        self.current_tip_position=p2

    def run_gcode3(self,p1,p2,c):
        lc=self.give_length_arc_circle(p1,p2,c,0)
        self.calculate_time_of_exection(lc)
        self.current_tip_position=p2

    def calculate_time_of_exection(self, lc):
        T=lc/(self.cnc.current_feed) * 60
        self.time=self.time+T

    def calculate_time_of_exection_2(self, lc):
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
