# Generated from Gcode.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GcodeParser import GcodeParser
else:
    from GcodeParser import GcodeParser

# This class defines a complete listener for a parse tree produced by GcodeParser.
class GcodeListener(ParseTreeListener):

    # Enter a parse tree produced by GcodeParser#prog.
    def enterProg(self, ctx:GcodeParser.ProgContext):
        pass

    # Exit a parse tree produced by GcodeParser#prog.
    def exitProg(self, ctx:GcodeParser.ProgContext):
        pass


    # Enter a parse tree produced by GcodeParser#expr.
    def enterExpr(self, ctx:GcodeParser.ExprContext):
        pass

    # Exit a parse tree produced by GcodeParser#expr.
    def exitExpr(self, ctx:GcodeParser.ExprContext):
        pass


    # Enter a parse tree produced by GcodeParser#stmt.
    def enterStmt(self, ctx:GcodeParser.StmtContext):
        pass

    # Exit a parse tree produced by GcodeParser#stmt.
    def exitStmt(self, ctx:GcodeParser.StmtContext):
        pass


    # Enter a parse tree produced by GcodeParser#gstmt.
    def enterGstmt(self, ctx:GcodeParser.GstmtContext):
        pass

    # Exit a parse tree produced by GcodeParser#gstmt.
    def exitGstmt(self, ctx:GcodeParser.GstmtContext):
        pass



del GcodeParser