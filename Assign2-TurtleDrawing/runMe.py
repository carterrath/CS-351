from antlr4 import *

from GCodesLexer import GCodesLexer
from GCodesParser import GCodesParser
from GCodesVisitor import GCodesVisitor
import time

def main():
        lexer = GCodesLexer( FileStream('GCodes_test'))
        token_stream = CommonTokenStream(lexer)
        parser = GCodesParser(token_stream)
        visitor = GCodesVisitor()

        while True:
                tree = parser.start()
                if tree.expr() == None: #meaning eof
                        break
                print(tree.toStringTree(recog=parser))
                visitor.visit(tree)

        time.sleep(2)

if __name__ == '__main__':
        main()
