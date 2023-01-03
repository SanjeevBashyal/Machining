# Generated from Sql.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#prog.
    def enterProg(self, ctx:SqlParser.ProgContext):
        pass

    # Exit a parse tree produced by SqlParser#prog.
    def exitProg(self, ctx:SqlParser.ProgContext):
        pass


    # Enter a parse tree produced by SqlParser#expr.
    def enterExpr(self, ctx:SqlParser.ExprContext):
        pass

    # Exit a parse tree produced by SqlParser#expr.
    def exitExpr(self, ctx:SqlParser.ExprContext):
        pass


    # Enter a parse tree produced by SqlParser#stmt.
    def enterStmt(self, ctx:SqlParser.StmtContext):
        pass

    # Exit a parse tree produced by SqlParser#stmt.
    def exitStmt(self, ctx:SqlParser.StmtContext):
        pass


    # Enter a parse tree produced by SqlParser#gstmt.
    def enterGstmt(self, ctx:SqlParser.GstmtContext):
        pass

    # Exit a parse tree produced by SqlParser#gstmt.
    def exitGstmt(self, ctx:SqlParser.GstmtContext):
        pass



del SqlParser