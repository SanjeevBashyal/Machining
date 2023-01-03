# Generated from Sql.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,25,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,5,1,
        14,8,1,10,1,12,1,17,9,1,1,2,1,2,3,2,21,8,2,1,3,1,3,1,3,0,0,4,0,2,
        4,6,0,0,22,0,8,1,0,0,0,2,15,1,0,0,0,4,20,1,0,0,0,6,22,1,0,0,0,8,
        9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,5,2,0,0,12,14,3,4,2,0,
        13,11,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,3,1,0,
        0,0,17,15,1,0,0,0,18,21,3,6,3,0,19,21,5,7,0,0,20,18,1,0,0,0,20,19,
        1,0,0,0,21,5,1,0,0,0,22,23,5,3,0,0,23,7,1,0,0,0,2,15,20
    ]

class SqlParser ( Parser ):

    grammarFileName = "Sql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "OID", "NID", "GID", "ID", "INT", "STRING", 
                      "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_stmt = 2
    RULE_gstmt = 3

    ruleNames =  [ "prog", "expr", "stmt", "gstmt" ]

    EOF = Token.EOF
    OID=1
    NID=2
    GID=3
    ID=4
    INT=5
    STRING=6
    COMMENT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SqlParser.ExprContext,0)


        def EOF(self):
            return self.getToken(SqlParser.EOF, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SqlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(SqlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NID(self, i:int=None):
            if i is None:
                return self.getTokens(SqlParser.NID)
            else:
                return self.getToken(SqlParser.NID, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SqlParser.StmtContext)
            else:
                return self.getTypedRuleContext(SqlParser.StmtContext,i)


        def getRuleIndex(self):
            return SqlParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SqlParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 11
                self.match(SqlParser.NID)
                self.state = 12
                self.stmt()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gstmt(self):
            return self.getTypedRuleContext(SqlParser.GstmtContext,0)


        def COMMENT(self):
            return self.getToken(SqlParser.COMMENT, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SqlParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.gstmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(SqlParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GID(self):
            return self.getToken(SqlParser.GID, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_gstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGstmt" ):
                listener.enterGstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGstmt" ):
                listener.exitGstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGstmt" ):
                return visitor.visitGstmt(self)
            else:
                return visitor.visitChildren(self)




    def gstmt(self):

        localctx = SqlParser.GstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_gstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(SqlParser.GID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





