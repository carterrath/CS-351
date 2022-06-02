grammar combat;
start : expr | <EOF>;

expr
	: '1v1' player1=PLAYER 'vs' player2=PLAYER #combat2playerExpr
        | 'multi' player1=PLAYER ('vs' addPlayer+=PLAYER)+ #combatMultiplayerExpr
        | 'timed' time=DURATION '->' player1=PLAYER ('vs' addPlayer+=PLAYER)+ #timedCombat
	;
PLAYER : (('A .. Z')|('a' .. 'z')|('0' .. '9'))+;
DURATION : ('0' .. '9')+ ('.' ('0' .. '9')+)?;

WS : [ \r\n\t]+ -> skip; 
