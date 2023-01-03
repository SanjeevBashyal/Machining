grammar Sql;
prog: expr EOF;
expr: (NID stmt)*;

stmt: gstmt | COMMENT;
// stmt: ((create_stmt | insert_stmt | select_stmt | delete_stmt) ';'+);

gstmt: GID;

OID: 'O'[0-9]+;
NID: 'N'[0-9]+;
GID: 'G'[0-9]+;


ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT : [0-9]+ ;
STRING: '"' (~('\n' | '"'))* '"';
COMMENT: '(' ~[\r\n]* ')'; //-> skip;
WS : [ \t\r\n] -> channel(HIDDEN);