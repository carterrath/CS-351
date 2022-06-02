# Generated from combat.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .combatParser import combatParser
else:
    from combatParser import combatParser

# This class defines a complete listener for a parse tree produced by combatParser.
class combatListener(ParseTreeListener):

    # Enter a parse tree produced by combatParser#start.
    def enterStart(self, ctx:combatParser.StartContext):
        pass

    # Exit a parse tree produced by combatParser#start.
    def exitStart(self, ctx:combatParser.StartContext):
        pass


    # Enter a parse tree produced by combatParser#combat2playerExpr.
    def enterCombat2playerExpr(self, ctx:combatParser.Combat2playerExprContext):
        pass

    # Exit a parse tree produced by combatParser#combat2playerExpr.
    def exitCombat2playerExpr(self, ctx:combatParser.Combat2playerExprContext):
        pass


    # Enter a parse tree produced by combatParser#combatMultiplayerExpr.
    def enterCombatMultiplayerExpr(self, ctx:combatParser.CombatMultiplayerExprContext):
        pass

    # Exit a parse tree produced by combatParser#combatMultiplayerExpr.
    def exitCombatMultiplayerExpr(self, ctx:combatParser.CombatMultiplayerExprContext):
        pass


    # Enter a parse tree produced by combatParser#timedCombat.
    def enterTimedCombat(self, ctx:combatParser.TimedCombatContext):
        pass

    # Exit a parse tree produced by combatParser#timedCombat.
    def exitTimedCombat(self, ctx:combatParser.TimedCombatContext):
        pass



del combatParser