# Generated from combat.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\6\7\61\n\7\r\7\16\7\62\3\b\6")
        buf.write("\b\66\n\b\r\b\16\b\67\3\b\3\b\6\b<\n\b\r\b\16\b=\5\b@")
        buf.write("\n\b\3\t\6\tC\n\t\r\t\16\tD\3\t\3\t\2\2\n\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\3\2\4\4\2\62;c|\5\2\13\f\17\17")
        buf.write("\"\"\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\3\23\3\2\2\2\5\27\3\2\2\2\7\32\3\2\2\2\t \3\2\2\2\13")
        buf.write("&\3\2\2\2\r\60\3\2\2\2\17\65\3\2\2\2\21B\3\2\2\2\23\24")
        buf.write("\7\63\2\2\24\25\7x\2\2\25\26\7\63\2\2\26\4\3\2\2\2\27")
        buf.write("\30\7x\2\2\30\31\7u\2\2\31\6\3\2\2\2\32\33\7o\2\2\33\34")
        buf.write("\7w\2\2\34\35\7n\2\2\35\36\7v\2\2\36\37\7k\2\2\37\b\3")
        buf.write("\2\2\2 !\7v\2\2!\"\7k\2\2\"#\7o\2\2#$\7g\2\2$%\7f\2\2")
        buf.write("%\n\3\2\2\2&\'\7/\2\2\'(\7@\2\2(\f\3\2\2\2)*\7C\2\2*+")
        buf.write("\7\"\2\2+,\7\60\2\2,-\7\60\2\2-.\7\"\2\2.\61\7\\\2\2/")
        buf.write("\61\t\2\2\2\60)\3\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60")
        buf.write("\3\2\2\2\62\63\3\2\2\2\63\16\3\2\2\2\64\66\4\62;\2\65")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28?")
        buf.write("\3\2\2\29;\7\60\2\2:<\4\62;\2;:\3\2\2\2<=\3\2\2\2=;\3")
        buf.write("\2\2\2=>\3\2\2\2>@\3\2\2\2?9\3\2\2\2?@\3\2\2\2@\20\3\2")
        buf.write("\2\2AC\t\3\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2")
        buf.write("EF\3\2\2\2FG\b\t\2\2G\22\3\2\2\2\t\2\60\62\67=?D\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class combatLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    PLAYER = 6
    DURATION = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'1v1'", "'vs'", "'multi'", "'timed'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "PLAYER", "DURATION", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "PLAYER", "DURATION", 
                  "WS" ]

    grammarFileName = "combat.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


