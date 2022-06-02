# Generated from combat.g4 by ANTLR 4.9
from antlr4 import *
import os
import shutil
import distutils.dir_util
import subprocess
if __name__ is not None and "." in __name__:
    from .combatParser import combatParser
else:
    from combatParser import combatParser

# This class defines a complete generic visitor for a parse tree produced by combatParser.

class combatVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by combatParser#start.
    def visitStart(self, ctx:combatParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by combatParser#combat2playerExpr.
    def visitCombat2playerExpr(self, ctx:combatParser.Combat2playerExprContext):
        #removes players directory
        shutil.rmtree("players/")
        #creates new players directory
        os.mkdir("players")
        #get players
        player1 = ctx.player1.text
        player2 = ctx.player2.text
        #define source  path
        source = "player_library/" + player1
        #define destination path
        destination = "players/" + player1
        #copy player files from source to destination
        distutils.dir_util.copy_tree(source, destination)
        #define source  path
        source = "player_library/" + player2
        #define destination path
        destination = "players/" + player2
        #copy player files from source to destination
        distutils.dir_util.copy_tree(source, destination)
        #run game
        os.system("python run_me.py")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by combatParser#combatMultiplayerExpr.
    def visitCombatMultiplayerExpr(self, ctx:combatParser.CombatMultiplayerExprContext):
        #removes players directory
        shutil.rmtree("players/")
        #creates new players directory
        os.mkdir("players")
        #get player1
        player1 = ctx.player1.text
        #define source  path
        source1 = "player_library/" + player1
        #define destination path
        destination1 = "players/" + player1
        #copy player files from source to destination
        distutils.dir_util.copy_tree(source1, destination1)
        #loop through addPlayer  list
        for i in range(len(ctx.addPlayer)):
            #get new player
            newPlayer = ctx.addPlayer[i].text
            #define source  path
            source2 = "player_library/" + newPlayer
            #define destination path
            destination2 = "players/" + newPlayer
            #copy player files from source to destination
            distutils.dir_util.copy_tree(source2, destination2)
        #run game
        os.system("python run_me.py")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by combatParser#timedCombat.
    def visitTimedCombat(self, ctx:combatParser.TimedCombatContext):
        try:
            #removes players directory
            shutil.rmtree("players/")
            #creates new players directory
            os.mkdir("players")
            #print(ctx.time.text)
            #get time
            time = float(ctx.time.text)
            #command to run file
            file = "python run_me.py"
            #print(time)
            #get player1
            player1 = ctx.player1.text
            #define source path
            source1 = "player_library/" + player1
            #define destination path
            destination1 = "players/" + player1
            #copy player files from source to destination
            distutils.dir_util.copy_tree(source1, destination1)
            #loop through addPlayer list
            for i in range(len(ctx.addPlayer)):
                newPlayer = ctx.addPlayer[i].text
                source2 = "player_library/" + newPlayer
                destination2 = "players/" + newPlayer
                distutils.dir_util.copy_tree(source2, destination2)

            #run game on a timeout. Works on windows, but not my mac
            #subprocess.check_output(file, timeout=time)

            #this runs on a timeout, but does not show the gamefield
            #subprocess.check_output('python run_me.py', shell=True, timeout=time)

            #this works on my mac but only freezes the gamefield and cannot exit program 
            subprocess.run(['python', 'run_me.py'], timeout=time)

        except subprocess.TimeoutExpired as e:
            print("timeout ended")
        return self.visitChildren(ctx)



del combatParser
