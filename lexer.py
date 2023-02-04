import ply.lex as lex

# List of token names
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
]

# Regular expressions for each token type
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Function to convert matched string of digits into an integer
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (whitespace)
t_ignore = " \t"

# Error handling function
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Create an instance of the lexer
lexer = lex.lex()
