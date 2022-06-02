# Generated from GCodes.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GCodesParser import GCodesParser
else:
    from GCodesParser import GCodesParser

# This class defines a complete listener for a parse tree produced by GCodesParser.
class GCodesListener(ParseTreeListener):

    # Enter a parse tree produced by GCodesParser#start.
    def enterStart(self, ctx:GCodesParser.StartContext):
        pass

    # Exit a parse tree produced by GCodesParser#start.
    def exitStart(self, ctx:GCodesParser.StartContext):
        pass


    # Enter a parse tree produced by GCodesParser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:GCodesParser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:GCodesParser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#changeColorExpr.
    def enterChangeColorExpr(self, ctx:GCodesParser.ChangeColorExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#changeColorExpr.
    def exitChangeColorExpr(self, ctx:GCodesParser.ChangeColorExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#feedRateExpr.
    def enterFeedRateExpr(self, ctx:GCodesParser.FeedRateExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#feedRateExpr.
    def exitFeedRateExpr(self, ctx:GCodesParser.FeedRateExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#drawCircleExpr.
    def enterDrawCircleExpr(self, ctx:GCodesParser.DrawCircleExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#drawCircleExpr.
    def exitDrawCircleExpr(self, ctx:GCodesParser.DrawCircleExprContext):
        pass


    # Enter a parse tree produced by GCodesParser#rotateCursor.
    def enterRotateCursor(self, ctx:GCodesParser.RotateCursorContext):
        pass

    # Exit a parse tree produced by GCodesParser#rotateCursor.
    def exitRotateCursor(self, ctx:GCodesParser.RotateCursorContext):
        pass


    # Enter a parse tree produced by GCodesParser#changeCursorShape.
    def enterChangeCursorShape(self, ctx:GCodesParser.ChangeCursorShapeContext):
        pass

    # Exit a parse tree produced by GCodesParser#changeCursorShape.
    def exitChangeCursorShape(self, ctx:GCodesParser.ChangeCursorShapeContext):
        pass


    # Enter a parse tree produced by GCodesParser#printlineExpr.
    def enterPrintlineExpr(self, ctx:GCodesParser.PrintlineExprContext):
        pass

    # Exit a parse tree produced by GCodesParser#printlineExpr.
    def exitPrintlineExpr(self, ctx:GCodesParser.PrintlineExprContext):
        pass



del GCodesParser