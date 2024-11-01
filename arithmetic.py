import ply.lex as lex
 
tokens=[
    'PRINT',
    'IDENTIFIER',
    'NUMBER',
    'ASSIGN',
    'OPERATOR',
    'STRING',
    'SEMICOLON',
    'NEWLINE',
    'CONCAT'
]

t_CONCAT=r'\.'
t_PRINT=r'PRINT'
t_IDENTIFIER=r'\$[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN=r'='
t_OPERATOR=r'[\+\-*/]'
t_SEMICOLON=r';'
t_ignore_PHP_TAGS = r'\<\?php|\?\>'
t_ignore_WHITESPACE =r'\s+'
t_ignore_COMMENT=r'//.*'

def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)?"'
    t.value = t.value.replace('"\n"','')
    if t.value=="":
        t.value=None
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno-2
    t.lexer.lineno +=len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

phpcode='''
<?php
$num1 = 10;
$num2 = 20;
$num3 = 30;
$sum = $num1 + $num2 + $num3;
$avg = $sum/3;
PRINT "Num1 is " . $num1 ."\n";
PRINT "Num2 is " . $num2 ."\n";
PRINT "Num3 is " . $num3 ."\n";
PRINT "Sum 3 numbers is " . $sum ."\n";
PRINT "Average is " . $avg;
?> 
'''

lexer=lex.lex()
lexer.input(phpcode)

for token in lexer:
    if token.type != 'NEWLINE'and token.value is not None:
        print(f"value {token.value} at line {token.lineno} TYPE: {token.type}")
