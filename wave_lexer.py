import ply.lex as lex

tokens = (
	'NUMBER',
	'SUM',
	'PRODUCT',
	'NEG',
	'INV',
	'LPAREN',
	'RPAREN',
	'LSQR',
	'RSQR'
)

t_SUM = r'\+'
t_PRODUCT = r'\*'
t_NEG = r'-'
t_INV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQR = r'\['
t_RSQR = r'\]'

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print("Illegal character {}".format(t.value[0]))
	t.lexer.skip(1)

lexer = lex.lex()