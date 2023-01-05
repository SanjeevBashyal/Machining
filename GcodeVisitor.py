# Generated from Gcode.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GcodeParser import GcodeParser
else:
    from GcodeParser import GcodeParser

# This class defines a complete generic visitor for a parse tree produced by GcodeParser.

class GcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GcodeParser#prog.
    def visitProg(self, ctx:GcodeParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GcodeParser#expr.
    def visitExpr(self, ctx:GcodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GcodeParser#stmt.
    def visitStmt(self, ctx:GcodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GcodeParser#gstmt.
    def visitGstmt(self, ctx:GcodeParser.GstmtContext):
        return self.visitChildren(ctx)



del GcodeParser