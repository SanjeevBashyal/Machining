grammar Gcode;
prog: OID expr EOF;
expr: (NID stmt)*;

stmt: (gstmt | COMMENT) ';'?;

gstmt: (GID | PID)+;

OID: 'O'[0-9]+;
NID: 'N'[0-9]+;
GID: [GTM][0-9]+;
PID: [HDFSPQXYZRIJK] (NEG)? [0-9]* (DOT)? [0-9]*;

DOT: '.';
NEG: '-';

COMMENT: '(' ~[\r\n]* ')'; //-> skip;
WS : [ \t\r\n] -> channel(HIDDEN);