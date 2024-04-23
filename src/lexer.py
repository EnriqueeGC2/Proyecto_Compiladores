import ply.lex as lex

open('bitacora_De_Errores.html', 'w').close()

# List of token names.  This is always required
tokens = [
    'ID',
    'NUMERO',
    'CADENA',
    # Data types
    'TIPO_DATO',
    'ENTERO',
    'REAL',
    'CARACTER',
    'LOGICO',
    # Keywords
    'ALGORITMO',
    'DEFINIR',
    'COMO',
    'HASTA',
    'CON_PASO',
    'FIN',
    # Procedures and functions
    'ESCRIBIR',
    'LEER',
    'PARA',
    'FUNCION',
    'MIENTRAS',
    'SEGUN',
    'HACER',
    'SI',
    'SI_NO',
    'RETORNAR',
    'DE_OTRO_MODO',
    'ENTONCES',
    'CONVERTIRATEXTO',
    'CONVERTIRANUMERO',
    'COMENTARIO',
    # Relational Operators
    'ES_MAYOR_QUE',
    'ES_MENOR_QUE',
    'ES_IGUAL_QUE',
    'ES_MAYOR_O_IGUAL_QUE',
    'ES_MENOR_O_IGUAL_QUE',
    'ES_DISTINTO_QUE',
    # Arithmetic Operators
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'ELEVADO_A',
    'RESIDUO',
    # Logical Operators
    'Y',
    'O',
    'NO',
    # Others
    'PUN_Y_COM',
    'COMA',
    'DOS_PUN',
    'PAR_IZQ',
    'PAR_DER',
    'COR_IZQ',
    'COR_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
]

def t_TIPO_DATO(t):
    r'(Entero|Real|Caracter|Logico)'
    return t

# Reserved words
def t_ALGORITMO(t):
    r'Algoritmo'
    return t

def t_DEFINIR(t):
    r'Definir'
    return t

def t_COMO(t):
    r'Como'
    return t

def t_HASTA(t):
    r'Hasta'
    return t

def t_CON_PASO(t):
    r'Con_Paso'
    return t

def t_FIN(t):
    r'Fin(Algoritmo|Funcion|Procedimiento|Si|Si_No|Mientras|Para|Segun)'
    return t

# Procedures and functions
def t_ESCRIBIR(t):
    r'Escribir'
    return t

def t_LEER(t):
    r'Leer'
    return t

def t_PARA(t):
    r'Para'
    return t

def t_FUNCION(t):
    r'Funcion'
    return t

def t_MIENTRAS(t):
    r'Mientras'
    return t

def t_SEGUN(t):
    r'Segun'
    return t

def t_HACER(t):
    r'Hacer'
    return t

def t_SI_NO(t):
    r'Si_No'
    return t

def t_SI(t):
    r'Si'
    return t

def t_RETORNAR(t):
    r'Retornar'
    return t

def t_DE_OTRO_MODO(t):
    r'De_Otro_Modo'
    return t

def t_ENTONCES(t):
    r'Entonces'
    return t

def t_CONVERTIRATEXTO(t):
    r'ConvertirATexto'
    return t

def t_CONVERTIRANUMERO(t):
    r'ConvertirANumero'
    return t

def t_COMENTARIO(t):
    r'//.*'
    return t

# Relational Operators
def t_ES_MAYOR_QUE(t):
    r'Es_Mayor_Que'
    return t

def t_ES_MENOR_QUE(t):
    r'Es_Menor_Que'
    return t

def t_ES_IGUAL_QUE(t):
    r'Es_Igual_Que'
    return t

def t_ES_MAYOR_O_IGUAL_QUE(t):
    r'Es_Mayor_O_Igual_Que'
    return t

def t_ES_MENOR_O_IGUAL_QUE(t):
    r'Es_Menor_O_Igual_Que'
    return t

def t_ES_DISTINTO_QUE(t):
    r'Es_Distinto_Que'
    return t

# Arithmetic Operators
def t_MAS(t):
    r'Mas'
    return t

def t_MENOS(t):
    r'Menos'
    return t

def t_POR(t):
    r'Por'
    return t

def t_DIVIDIDO(t):
    r'Dividido'
    return t

def t_ELEVADO_A(t):
    r'Elevado_A'
    return t

def t_RESIDUO(t):
    r'Residuo'
    return t

# Logical Operators
def t_Y(t):
    r'Y'
    return t

def t_O(t):
    r'O'
    return t

def t_NO(t):
    r'No'
    return t

# Others
def t_PAR_IZQ(t):
    r'Par_Izq'
    return t

def t_PAR_DER(t):
    r'Par_Der'
    return t

def t_COR_IZQ(t): # Corchete
    r'Cor_Izq'
    return t

def t_COR_DER(t):
    r'Cor_Der'
    return t

def t_LLAVE_IZQ(t):
    r'Llave_Izq'
    return t

def t_LLAVE_DER(t):
    r'Llave_Der'
    return t

def t_PUN_Y_COM(t):
    r'Pun_Y_Com'
    return t

def t_COMA(t):
    r'COMA'
    return t

def t_DOS_PUN(t):
    r'Dos_Pun'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'A_Com .* C_Com'
    return t

def t_ID(t):
    r'[a-z][_a-z_A-Z_0-9]*'  # Identificadores que comienzan con una letra minúscula
    return t

t_ignore = ' \t'

def t_INITIAL_last_newline_pos(t):
    r'.'
    t.lexer.last_newline_pos = 0

def t_newlline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #t.lexer.last_newline_pos = t.lexer.lexpos - len(t.value)

def t_INITIAL_UPPERCASE_ERROR(t):
    r'[A-Z][a-zA-Z_0-9]*'  # Identificadores que comienzan con una letra mayúscula
    print(f'Error: {t.value} no es un identificador valido., en la linea {t.lineno} y columna {t.lexpos}.')
    with open('bitacora_De_Errores.html', 'a') as file:
        file.write(f'Error: {t.value} no es un identificador valido, en la linea {t.lineno} y columna {t.lexpos}.\n')
    t.lexer.skip(1)

def t_error(t):
    #print(f'Error: Caracter inesperado "{t.value[0]}".')
    with open('bitacora_De_Errores.html', 'a') as file:
        file.write(f'Error: Caracter inesperado "{t.value[0]}, en la linea: {t.lineno} y la posicion: {t.lexpos}".\n')
    t.lexer.skip(1)

def readFile(fileName):
    with open(fileName, 'r') as file:
        return file.read()

def getTokens():
    num = 0
    with open('tokens.html', 'w') as file:
        for token in tokensEncontrados:
            num += 1
            file.write(f'<p>{num}) Token encontrado -> " {token.value} ", en la linea: {token.lineno}, en la posicion: {token.lexpos} </p>\n')

def test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokensEncontrados.append(tok)
        print(tok, f"Linea: {tok.lineno}, en la posicion: {tok.lexpos}")

tokensEncontrados = []

lexer = lex.lex()
"""
if __name__ == '__main__':
    fileName = 'codigo_fuente.txt'
    data = readFile(fileName)

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokensEncontrados.append(tok)
        print(tok, f"Linea: {tok.lineno}, en la posicion: {tok.lexpos}")

    getTokens()
"""