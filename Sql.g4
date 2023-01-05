grammar Sql;
prog: OID expr EOF;
expr: (NID stmt)*;

stmt: gstmt | COMMENT;

gstmt: GID* (PID)*;

OID: 'O'[0-9]+;
NID: 'N'[0-9]+;
GID: [GTM][0-9]+;
PID: [FSXYZIJK] (NEG)? [0-9]+ (DOT)? [0-9]*;
// YID: 'Y' (NEG)? [0-9]+ (DOT)? [0-9]*;
// IID: 'I' (NEG)? [0-9]+ (DOT)? [0-9]*;
// JID: 'J' (NEG)? [0-9]+ (DOT)? [0-9]*;

DOT: '.';
NEG: '-';

// ID: [a-zA-Z_][a-zA-Z0-9_]*;
// INT : [0-9]+ ;
// STRING: '"' (~('\n' | '"'))* '"';
COMMENT: '(' ~[\r\n]* ')'; //-> skip;
WS : [ \t\r\n] -> channel(HIDDEN);