# Generated from combat.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("#\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\6\3\23\n\3\r\3\16\3\24\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\6\3\35\n\3\r\3\16\3\36\5\3!\n\3\3\3\2\2\4\2\4")
        buf.write("\2\2\2%\2\b\3\2\2\2\4 \3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2")
        buf.write("\b\6\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13\f")
        buf.write("\7\b\2\2\f\r\7\4\2\2\r!\7\b\2\2\16\17\7\5\2\2\17\22\7")
        buf.write("\b\2\2\20\21\7\4\2\2\21\23\7\b\2\2\22\20\3\2\2\2\23\24")
        buf.write("\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25!\3\2\2\2\26\27")
        buf.write("\7\6\2\2\27\30\7\t\2\2\30\31\7\7\2\2\31\34\7\b\2\2\32")
        buf.write("\33\7\4\2\2\33\35\7\b\2\2\34\32\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2 \n\3\2\2\2 \16")
        buf.write("\3\2\2\2 \26\3\2\2\2!\5\3\2\2\2\6\b\24\36 ")
        return buf.getvalue()


class combatParser ( Parser ):

    grammarFileName = "combat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'1v1'", "'vs'", "'multi'", "'timed'", 
                     "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PLAYER", "DURATION", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    PLAYER=6
    DURATION=7
    WS=8

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
            return self.getTypedRuleContext(combatParser.ExprContext,0)


        def getRuleIndex(self):
            return combatParser.RULE_start

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

        localctx = combatParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [combatParser.T__0, combatParser.T__2, combatParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [combatParser.EOF]:
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
            return combatParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TimedCombatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a combatParser.ExprContext
            super().__init__(parser)
            self.time = None # Token
            self.player1 = None # Token
            self._PLAYER = None # Token
            self.addPlayer = list() # of Tokens
            self.copyFrom(ctx)

        def DURATION(self):
            return self.getToken(combatParser.DURATION, 0)
        def PLAYER(self, i:int=None):
            if i is None:
                return self.getTokens(combatParser.PLAYER)
            else:
                return self.getToken(combatParser.PLAYER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimedCombat" ):
                listener.enterTimedCombat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimedCombat" ):
                listener.exitTimedCombat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimedCombat" ):
                return visitor.visitTimedCombat(self)
            else:
                return visitor.visitChildren(self)


    class CombatMultiplayerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a combatParser.ExprContext
            super().__init__(parser)
            self.player1 = None # Token
            self._PLAYER = None # Token
            self.addPlayer = list() # of Tokens
            self.copyFrom(ctx)

        def PLAYER(self, i:int=None):
            if i is None:
                return self.getTokens(combatParser.PLAYER)
            else:
                return self.getToken(combatParser.PLAYER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombatMultiplayerExpr" ):
                listener.enterCombatMultiplayerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombatMultiplayerExpr" ):
                listener.exitCombatMultiplayerExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombatMultiplayerExpr" ):
                return visitor.visitCombatMultiplayerExpr(self)
            else:
                return visitor.visitChildren(self)


    class Combat2playerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a combatParser.ExprContext
            super().__init__(parser)
            self.player1 = None # Token
            self.player2 = None # Token
            self.copyFrom(ctx)

        def PLAYER(self, i:int=None):
            if i is None:
                return self.getTokens(combatParser.PLAYER)
            else:
                return self.getToken(combatParser.PLAYER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombat2playerExpr" ):
                listener.enterCombat2playerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombat2playerExpr" ):
                listener.exitCombat2playerExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombat2playerExpr" ):
                return visitor.visitCombat2playerExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = combatParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [combatParser.T__0]:
                localctx = combatParser.Combat2playerExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(combatParser.T__0)
                self.state = 9
                localctx.player1 = self.match(combatParser.PLAYER)
                self.state = 10
                self.match(combatParser.T__1)
                self.state = 11
                localctx.player2 = self.match(combatParser.PLAYER)
                pass
            elif token in [combatParser.T__2]:
                localctx = combatParser.CombatMultiplayerExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(combatParser.T__2)
                self.state = 13
                localctx.player1 = self.match(combatParser.PLAYER)
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 14
                    self.match(combatParser.T__1)
                    self.state = 15
                    localctx._PLAYER = self.match(combatParser.PLAYER)
                    localctx.addPlayer.append(localctx._PLAYER)
                    self.state = 18 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==combatParser.T__1):
                        break

                pass
            elif token in [combatParser.T__3]:
                localctx = combatParser.TimedCombatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(combatParser.T__3)
                self.state = 21
                localctx.time = self.match(combatParser.DURATION)
                self.state = 22
                self.match(combatParser.T__4)
                self.state = 23
                localctx.player1 = self.match(combatParser.PLAYER)
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 24
                    self.match(combatParser.T__1)
                    self.state = 25
                    localctx._PLAYER = self.match(combatParser.PLAYER)
                    localctx.addPlayer.append(localctx._PLAYER)
                    self.state = 28 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==combatParser.T__1):
                        break

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





