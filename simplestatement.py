import ply.lex as lex

tokens=[
    'PRINT',
    'ECHO',
    'STRING',
    'SEMICOLON',
    'NEWLINE'
]

t_PRINT =r'PRINT'
t_ECHO = r'ECHO'
t_STRING =r'"([^"\\]*(\\.[^"\\]*)*)"'
t_SEMICOLON =r';'
t_ignore_PHP_TAGS = r'\<\?php|\?\>'
t_ignore_WHITESPACE =r'\s+'
t_ignore_COMMENT=r'//.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno +=len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer=lex.lex()

phpcode='''
<?php //php 7.2.24
PRINT "Hello, world! \\n";
ECHO "Welcome "
?>
'''

lexer.input(phpcode)

for token in lexer:
    print(f"value {token.value} at line {token.lineno} TYPE: {token.type}")
