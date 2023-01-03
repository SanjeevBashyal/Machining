grammar Sql;
prog: expr EOF;
expr: stmt*;

stmt: ((create_stmt | insert_stmt | select_stmt | delete_stmt) ';'+)
;

create_stmt: 'CREATE' 'table' ID '(' column_list ')' ;
column_list: column_spec ( ',' column_spec )* ;
column_spec: ID ':' column_type;
column_type: 'string' | 'int';

insert_stmt: 'INSERT' 'INTO' ID '(' VAL ( ',' VAL )* ')' ;
VAL : INT | STRING ;

select_stmt: 'SELECT' (min_max | ids) 'FROM' ID ('WHERE' cond (LOP cond)*)*;
cond : ID (OP) VAL ;
min_max: MINMAX '(' ID ')';
ids:((ID (',' ID)*) | '*');
MINMAX: 'MIN' | 'MAX' | 'COUNT';

delete_stmt: 'DELETE' 'FROM' ID ('WHERE' cond (LOP cond)*)*;

LOP: 'OR'| 'AND';
OP: EQ | GR | LS | GEQ | LEQ | NEQ;
EQ: '=';
GR: '>';
LS: '<';
GEQ: '>=';
LEQ: '<=';
NEQ: '!=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT : [0-9]+ ;
STRING: '"' (~('\n' | '"'))* '"';
COMMENT: '//' ~[\r\n]* -> skip;
WS : [ \t\r\n] -> channel(HIDDEN);