from antlr4 import *

from combatLexer import combatLexer
from combatParser import combatParser
from combatVisitor import combatVisitor
import time

def main():
        lexer = combatLexer( FileStream('combat_test'))
        token_stream = CommonTokenStream(lexer)
        parser = combatParser(token_stream)
        visitor = combatVisitor()

        while True:
                tree = parser.start()
                if tree.expr() == None: #meaning eof
                        break
                print(tree.toStringTree(recog=parser))
                visitor.visit(tree)

        time.sleep(2)

if __name__ == '__main__':
        main()
