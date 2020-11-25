grammar MiniC;

prog: function* EOF #progRule;

// For now, we don't have "real" functions, just the main() function
// that is the main program, with a hardcoded profile and final
// 'return 0'.
function: INTTYPE ID OPAR CPAR OBRACE vardecl_l block
	RETURN INT SCOL CBRACE #funcDecl;

vardecl_l: vardecl* #varDeclList;

vardecl: typee id_l SCOL #varDecl;



id_l
    : ID              #idListBase
    | ID COM id_l     #idList
    ;

block: stat*   #statList;

stat
    : assignment
    | if_stat
    | while_stat
    | print_stat
    | assert_stat
    | OTHER {print("unknown char: {}".format($OTHER.text))}
    ;

assignment: ID ASSIGN expr SCOL #assignStat;

if_stat: IF condition_block (ELSE IF condition_block)* (ELSE stat_block)? #ifStat;

condition_block: expr stat_block  #condBlock;

stat_block
    : OBRACE block CBRACE
    | stat
    ;

while_stat: WHILE expr stat_block #whileStat;




assert_stat
    : ASSERT OPAR expr CPAR SCOL #assertStat;

print_stat
    : PRINTINT OPAR expr CPAR SCOL         #printintStat
    | PRINTFLOAT OPAR expr CPAR SCOL       #printfloatStat
    | PRINTSTRING OPAR expr CPAR SCOL      #printstringStat
    ;

expr_l
    : /* Nothing */     #exprListEmpty
    | expr              #exprListBase
    | expr COM expr_l   #exprList
    ;


expr
    : MINUS expr                           	 #unaryMinusExpr
    | NOT expr                             	 #notExpr
    | expr myop=(MULT|DIV|MOD)  expr       	 #multiplicativeExpr
    | expr myop=(PLUS|MINUS) expr          	 #additiveExpr
    | expr myop=(GT|LT|GTEQ|LTEQ|EQ|NEQ) expr    #relationalExpr
    | expr AND expr                        	 #andExpr
    | expr OR expr                         	 #orExpr
    | atom                                 	 #atomExpr
    | RAND OPAR expr COM expr CPAR	   #randExpr
    ;

atom
    : OPAR expr CPAR #parExpr
    | (INT | FLOAT)  #numberAtom
    | (TRUE | FALSE) #booleanAtom
    | ID             #idAtom
    | STRING         #stringAtom
    ;

typee
    : mytype=(INTTYPE|FLOATTYPE|BOOLTYPE|STRINGTYPE) #basicType
    ;

RAND : 'rand';
ASSERT : 'assert';
OR : '||';
AND : '&&';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD : '%';
NOT : '!';

COL: ':';
SCOL : ';';
COM : ',';
ASSIGN : '=';
OPAR : '(';
CPAR : ')';
OBRACE : '{';
CBRACE : '}';

TRUE : 'true';
FALSE : 'false';
IF : 'if';
ELSE : 'else';
WHILE : 'while';

RETURN : 'return';
PRINTINT : 'println_int';
PRINTSTRING : 'println_string';
PRINTFLOAT : 'println_float';

INTTYPE: 'int';
FLOATTYPE: 'float';
STRINGTYPE: 'string';
BOOLTYPE : 'bool';

ID
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

INT
 : [0-9]+
 ;

FLOAT
 : [0-9]+ '.' [0-9]* 
 | '.' [0-9]+
 ;

STRING
 : '"' (~["\r\n] | '""')* '"'
 ;


COMMENT
// # is a comment in Mini-C, and used for #include in real C so that we ignore #include statements
 : ('#' | '//') ~[\r\n]* -> skip
 ;


SPACE
 : [ \t\r\n] -> skip
 ;

OTHER
 : . 
 ;
