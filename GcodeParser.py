# Generated from Gcode.g4 by ANTLR 4.11.1
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
        4,1,9,32,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,3,2,22,8,2,1,2,3,2,25,8,2,1,
        3,4,3,28,8,3,11,3,12,3,29,1,3,0,0,4,0,2,4,6,0,1,1,0,4,5,31,0,8,1,
        0,0,0,2,16,1,0,0,0,4,21,1,0,0,0,6,27,1,0,0,0,8,9,5,2,0,0,9,10,3,
        2,1,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,5,3,0,0,13,15,3,4,2,0,14,
        12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,3,1,0,0,
        0,18,16,1,0,0,0,19,22,3,6,3,0,20,22,5,8,0,0,21,19,1,0,0,0,21,20,
        1,0,0,0,22,24,1,0,0,0,23,25,5,1,0,0,24,23,1,0,0,0,24,25,1,0,0,0,
        25,5,1,0,0,0,26,28,7,0,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,
        0,0,29,30,1,0,0,0,30,7,1,0,0,0,4,16,21,24,29
    ]

class GcodeParser ( Parser ):

    grammarFileName = "Gcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "OID", "NID", "GID", "PID", 
                      "DOT", "NEG", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_stmt = 2
    RULE_gstmt = 3

    ruleNames =  [ "prog", "expr", "stmt", "gstmt" ]

    EOF = Token.EOF
    T__0=1
    OID=2
    NID=3
    GID=4
    PID=5
    DOT=6
    NEG=7
    COMMENT=8
    WS=9

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
            return self.getToken(GcodeParser.OID, 0)

        def expr(self):
            return self.getTypedRuleContext(GcodeParser.ExprContext,0)


        def EOF(self):
            return self.getToken(GcodeParser.EOF, 0)

        def getRuleIndex(self):
            return GcodeParser.RULE_prog

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

        localctx = GcodeParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(GcodeParser.OID)
            self.state = 9
            self.expr()
            self.state = 10
            self.match(GcodeParser.EOF)
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
                return self.getTokens(GcodeParser.NID)
            else:
                return self.getToken(GcodeParser.NID, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GcodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(GcodeParser.StmtContext,i)


        def getRuleIndex(self):
            return GcodeParser.RULE_expr

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

        localctx = GcodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 12
                self.match(GcodeParser.NID)
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
            return self.getTypedRuleContext(GcodeParser.GstmtContext,0)


        def COMMENT(self):
            return self.getToken(GcodeParser.COMMENT, 0)

        def getRuleIndex(self):
            return GcodeParser.RULE_stmt

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

        localctx = GcodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                self.state = 19
                self.gstmt()
                pass
            elif token in [8]:
                self.state = 20
                self.match(GcodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 23
                self.match(GcodeParser.T__0)


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
                return self.getTokens(GcodeParser.GID)
            else:
                return self.getToken(GcodeParser.GID, i)

        def PID(self, i:int=None):
            if i is None:
                return self.getTokens(GcodeParser.PID)
            else:
                return self.getToken(GcodeParser.PID, i)

        def getRuleIndex(self):
            return GcodeParser.RULE_gstmt

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

        localctx = GcodeParser.GstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_gstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





