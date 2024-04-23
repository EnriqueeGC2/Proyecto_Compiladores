import ply.yacc as yacc

from lexer import tokens
from symbol_table import insertSymbol, getSymbol

def p_program(p):
    'program : PROGRAM ID PUN_Y_COM program_body'
    insertSymbol(p[2], 'program', p.lineno(2), p.lexpos(2))
