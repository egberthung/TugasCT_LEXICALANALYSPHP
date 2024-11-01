import ply.lex as lex
 
tokens=[
    'PRINT',
    'IDENTIFIER',
    'NUMBER',
    'ASSIGN',
    'OPERATOR',
    'STRING',
    'SEMICOLON',
    'CONDITION',
    'RELATIONOPERATION',
    'NEWLINE',
    'LOOP',
    'BRACE',
    'PAREN',
    'CONCAT'
]

t_PRINT=r'PRINT'
t_IDENTIFIER=r'\$[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN=r'='
t_SEMICOLON=r';'
t_LOOP=r'WHILE|FOR'
t_CONDITION=r'IF|ELSE|ELSEIF'
t_CONCAT=r'\.'
t_RELATIONOPERATION=r'==|!=|<=|>=|<|>'
t_BRACE=r'[{}]'
t_PAREN=r'[()]'
t_OPERATOR = r'[\+\-*/\%]'

t_ignore_WHITESPACE =r'\s+'

def t_ignore_COMMENT(t):
    r'//.*'
    pass

def t_ignore_PHP_TAGS(t):
    r'\<\?php|\?\>'
    lexer.lineno =0
    pass

def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    t.value = t.value.replace('"\n"','')
    if t.value=="" or t.value=='""':
        t.value=None
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno +=len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

phpcode='''<?php //php 7.2.24
PRINT "List of Odd Number 1-100:\n";
PRINT "\n";
$num=1;
WHILE ($num<=100) {
IF (($num % 2)!=0) {
$oddnum=$num;
PRINT "".$num." "; }
$num=$num+1;
}
?>
'''

lexer=lex.lex()

lexer.input(phpcode)

for token in lexer:
    if token.type != 'NEWLINE' and token.value is not None:
        print(f"value {token.value} at line {token.lineno} TYPE: {token.type}")
