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
        4,1,8,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,3,2,22,8,2,1,3,5,3,25,8,3,10,
        3,12,3,28,9,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,3,0,0,4,0,2,4,6,
        0,0,35,0,8,1,0,0,0,2,16,1,0,0,0,4,21,1,0,0,0,6,26,1,0,0,0,8,9,5,
        1,0,0,9,10,3,2,1,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,5,2,0,0,13,15,
        3,4,2,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,
        17,3,1,0,0,0,18,16,1,0,0,0,19,22,3,6,3,0,20,22,5,7,0,0,21,19,1,0,
        0,0,21,20,1,0,0,0,22,5,1,0,0,0,23,25,5,3,0,0,24,23,1,0,0,0,25,28,
        1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,32,1,0,0,0,28,26,1,0,0,0,
        29,31,5,4,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,
        0,0,0,33,7,1,0,0,0,34,32,1,0,0,0,4,16,21,26,32
    ]

class SqlParser ( Parser ):

    grammarFileName = "Sql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "'-'" ]

    symbolicNames = [ "<INVALID>", "OID", "NID", "GID", "PID", "DOT", "NEG", 
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
    PID=4
    DOT=5
    NEG=6
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

        def OID(self):
            return self.getToken(SqlParser.OID, 0)

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
            self.match(SqlParser.OID)
            self.state = 9
            self.expr()
            self.state = 10
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
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 12
                self.match(SqlParser.NID)
                self.state = 13
                self.stmt()
                self.state = 18
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
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.gstmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
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

        def GID(self, i:int=None):
            if i is None:
                return self.getTokens(SqlParser.GID)
            else:
                return self.getToken(SqlParser.GID, i)

        def PID(self, i:int=None):
            if i is None:
                return self.getTokens(SqlParser.PID)
            else:
                return self.getToken(SqlParser.PID, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 23
                self.match(SqlParser.GID)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 29
                self.match(SqlParser.PID)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





