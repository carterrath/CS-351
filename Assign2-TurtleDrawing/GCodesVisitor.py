# Generated from GCodes.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GCodesParser import GCodesParser
else:
    from GCodesParser import GCodesParser

import turtle
skk =  turtle.Turtle()

# This class defines a complete generic visitor for a parse tree produced by GCodesParser.

class GCodesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GCodesParser#start.
    def visitStart(self, ctx:GCodesParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:GCodesParser.DrawlineExprContext):
        target_x = float(ctx.x_cord.text)
        target_y = float(ctx.y_cord.text)
        cur_x_pos  = skk.xcor() #(x,y)
        cur_y_pos  = skk.ycor()
        if cur_x_pos == 0:
            if cur_y_pos == 0:
                skk.penup()
        else:
            skk.pendown()
        skk.goto(target_x, target_y)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GCodesParser#changeColorExpr.
    def visitChangeColorExpr(self, ctx:GCodesParser.ChangeColorExprContext):
        skk.pencolor(ctx.z_cord.text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#feedRateExpr.
    def visitFeedRateExpr(self, ctx:GCodesParser.FeedRateExprContext):
        skk.speed(float(ctx.feed.text))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#drawCircleExpr.
    def visitDrawCircleExpr(self, ctx:GCodesParser.DrawCircleExprContext):
        skk.circle(float(ctx.radius.text))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#rotateCursor.
    def visitRotateCursor(self, ctx:GCodesParser.RotateCursorContext):
        degrees = float(ctx.rotate.text)
        if degrees > 0:
            skk.right(degrees)
        else:
            skk.left(degrees * (-1))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#changeCursorShape.
    def visitChangeCursorShape(self, ctx:GCodesParser.ChangeCursorShapeContext):
        skk.shape(ctx.shape.text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GCodesParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:GCodesParser.PrintlineExprContext):

        return self.visitChildren(ctx)

del GCodesParser
