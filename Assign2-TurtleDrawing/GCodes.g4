grammar GCodes;

start : expr | <EOF>;

expr
	: 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr
	| 'Z' z_cord=WORD #changeColorExpr
	| 'F' feed=NUMBER #feedRateExpr
	| 'G02' radius=NUMBER #drawCircleExpr
	| 'A' rotate=NUMBER #rotateCursor
	| 'T' shape=WORD #changeCursorShape
	| 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr
	;

NUMBER : ('-')? ('0' .. '9') + ('.' ('0' .. '9')+)?;

WORD : (('A' .. 'Z')|('a' .. 'z'))+;

WS : [ \r\n\t]+ -> skip;

