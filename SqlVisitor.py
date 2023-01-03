# Generated from Sql.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.

class SqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#prog.
    def visitProg(self, ctx:SqlParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#expr.
    def visitExpr(self, ctx:SqlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#stmt.
    def visitStmt(self, ctx:SqlParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#gstmt.
    def visitGstmt(self, ctx:SqlParser.GstmtContext):
        return self.visitChildren(ctx)



del SqlParser