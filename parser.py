import ply.yacc as yacc
from lexer import tokens

# Grammar rule for parsing an expression with a PLUS operator
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

# Grammar rule for parsing an expression with a MINUS operator
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

# Grammar rule for parsing a term as an expression
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

# Grammar rule for parsing a term with a TIMES operator
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

# Grammar rule for parsing a term with a DIVIDE operator
def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

# Grammar rule for parsing a factor as a term
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# Grammar rule for parsing a factor as a number
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

# Grammar rule for parsing a factor as an expression in parentheses
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error handling function
def p_error(p):
    print("Syntax error in input!")

# Create an instance of the parser
parser = yacc.yacc()
