# Generated from GCodes.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\5\t/\n\t\3\t\6\t\62\n\t\r\t\16\t\63")
        buf.write("\3\t\3\t\6\t8\n\t\r\t\16\t9\5\t<\n\t\3\n\6\n?\n\n\r\n")
        buf.write("\16\n@\3\13\6\13D\n\13\r\13\16\13E\3\13\3\13\2\2\f\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\4\4\2C")
        buf.write("\\c|\5\2\13\f\17\17\"\"\2N\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2")
        buf.write("\2\5\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13#\3\2\2\2")
        buf.write("\r%\3\2\2\2\17\'\3\2\2\2\21.\3\2\2\2\23>\3\2\2\2\25C\3")
        buf.write("\2\2\2\27\30\7I\2\2\30\31\7\62\2\2\31\32\7\63\2\2\32\4")
        buf.write("\3\2\2\2\33\34\7\\\2\2\34\6\3\2\2\2\35\36\7H\2\2\36\b")
        buf.write("\3\2\2\2\37 \7I\2\2 !\7\62\2\2!\"\7\64\2\2\"\n\3\2\2\2")
        buf.write("#$\7C\2\2$\f\3\2\2\2%&\7V\2\2&\16\3\2\2\2\'(\7r\2\2()")
        buf.write("\7t\2\2)*\7k\2\2*+\7p\2\2+,\7v\2\2,\20\3\2\2\2-/\7/\2")
        buf.write("\2.-\3\2\2\2./\3\2\2\2/\61\3\2\2\2\60\62\4\62;\2\61\60")
        buf.write("\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64")
        buf.write(";\3\2\2\2\65\67\7\60\2\2\668\4\62;\2\67\66\3\2\2\289\3")
        buf.write("\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;\65\3\2\2\2;<\3")
        buf.write("\2\2\2<\22\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2")
        buf.write("\2\2@A\3\2\2\2A\24\3\2\2\2BD\t\3\2\2CB\3\2\2\2DE\3\2\2")
        buf.write("\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\13\2\2H\26\3\2\2")
        buf.write("\2\n\2.\639;>@E\3\b\2\2")
        return buf.getvalue()


class GCodesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    NUMBER = 8
    WORD = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'Z'", "'F'", "'G02'", "'A'", "'T'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WORD", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NUMBER", "WORD", "WS" ]

    grammarFileName = "GCodes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


