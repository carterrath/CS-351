# Generated from GCodes.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\35\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\33")
        buf.write("\n\3\3\3\2\2\4\2\4\2\2\2!\2\b\3\2\2\2\4\32\3\2\2\2\6\t")
        buf.write("\5\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2")
        buf.write("\2\n\13\7\3\2\2\13\f\7\n\2\2\f\33\7\n\2\2\r\16\7\4\2\2")
        buf.write("\16\33\7\13\2\2\17\20\7\5\2\2\20\33\7\n\2\2\21\22\7\6")
        buf.write("\2\2\22\33\7\n\2\2\23\24\7\7\2\2\24\33\7\n\2\2\25\26\7")
        buf.write("\b\2\2\26\33\7\13\2\2\27\30\7\t\2\2\30\31\7\n\2\2\31\33")
        buf.write("\7\n\2\2\32\n\3\2\2\2\32\r\3\2\2\2\32\17\3\2\2\2\32\21")
        buf.write("\3\2\2\2\32\23\3\2\2\2\32\25\3\2\2\2\32\27\3\2\2\2\33")
        buf.write("\5\3\2\2\2\4\b\32")
        return buf.getvalue()


class GCodesParser ( Parser ):

    grammarFileName = "GCodes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'Z'", "'F'", "'G02'", "'A'", 
                     "'T'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WORD", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    WORD=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GCodesParser.ExprContext,0)


        def getRuleIndex(self):
            return GCodesParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = GCodesParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GCodesParser.T__0, GCodesParser.T__1, GCodesParser.T__2, GCodesParser.T__3, GCodesParser.T__4, GCodesParser.T__5, GCodesParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [GCodesParser.EOF]:
                self.enterOuterAlt(localctx, 2)

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


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GCodesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ChangeCursorShapeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.shape = None # Token
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(GCodesParser.WORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChangeCursorShape" ):
                listener.enterChangeCursorShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChangeCursorShape" ):
                listener.exitChangeCursorShape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChangeCursorShape" ):
                return visitor.visitChangeCursorShape(self)
            else:
                return visitor.visitChildren(self)


    class ChangeColorExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.z_cord = None # Token
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(GCodesParser.WORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChangeColorExpr" ):
                listener.enterChangeColorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChangeColorExpr" ):
                listener.exitChangeColorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChangeColorExpr" ):
                return visitor.visitChangeColorExpr(self)
            else:
                return visitor.visitChildren(self)


    class RotateCursorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.rotate = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(GCodesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRotateCursor" ):
                listener.enterRotateCursor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRotateCursor" ):
                listener.exitRotateCursor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRotateCursor" ):
                return visitor.visitRotateCursor(self)
            else:
                return visitor.visitChildren(self)


    class FeedRateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.feed = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(GCodesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeedRateExpr" ):
                listener.enterFeedRateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeedRateExpr" ):
                listener.exitFeedRateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeedRateExpr" ):
                return visitor.visitFeedRateExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawCircleExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.radius = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(GCodesParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawCircleExpr" ):
                listener.enterDrawCircleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawCircleExpr" ):
                listener.exitDrawCircleExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawCircleExpr" ):
                return visitor.visitDrawCircleExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrintlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GCodesParser.NUMBER)
            else:
                return self.getToken(GCodesParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlineExpr" ):
                listener.enterPrintlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlineExpr" ):
                listener.exitPrintlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlineExpr" ):
                return visitor.visitPrintlineExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GCodesParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GCodesParser.NUMBER)
            else:
                return self.getToken(GCodesParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawlineExpr" ):
                listener.enterDrawlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawlineExpr" ):
                listener.exitDrawlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawlineExpr" ):
                return visitor.visitDrawlineExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = GCodesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GCodesParser.T__0]:
                localctx = GCodesParser.DrawlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(GCodesParser.T__0)
                self.state = 9
                localctx.x_cord = self.match(GCodesParser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(GCodesParser.NUMBER)
                pass
            elif token in [GCodesParser.T__1]:
                localctx = GCodesParser.ChangeColorExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(GCodesParser.T__1)
                self.state = 12
                localctx.z_cord = self.match(GCodesParser.WORD)
                pass
            elif token in [GCodesParser.T__2]:
                localctx = GCodesParser.FeedRateExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(GCodesParser.T__2)
                self.state = 14
                localctx.feed = self.match(GCodesParser.NUMBER)
                pass
            elif token in [GCodesParser.T__3]:
                localctx = GCodesParser.DrawCircleExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 15
                self.match(GCodesParser.T__3)
                self.state = 16
                localctx.radius = self.match(GCodesParser.NUMBER)
                pass
            elif token in [GCodesParser.T__4]:
                localctx = GCodesParser.RotateCursorContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 17
                self.match(GCodesParser.T__4)
                self.state = 18
                localctx.rotate = self.match(GCodesParser.NUMBER)
                pass
            elif token in [GCodesParser.T__5]:
                localctx = GCodesParser.ChangeCursorShapeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 19
                self.match(GCodesParser.T__5)
                self.state = 20
                localctx.shape = self.match(GCodesParser.WORD)
                pass
            elif token in [GCodesParser.T__6]:
                localctx = GCodesParser.PrintlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 21
                self.match(GCodesParser.T__6)
                self.state = 22
                localctx.x_cord = self.match(GCodesParser.NUMBER)
                self.state = 23
                localctx.y_cord = self.match(GCodesParser.NUMBER)
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





