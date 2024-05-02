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
    # FIN
    'FIN_ALGORITMO',
    'FIN_FUNCION',
    'FIN_PROCEDIMIENTO',
    'FIN_SI',
    'FIN_SI_NO',
    'FIN_MIENTRAS',
    'FIN_PARA',
    'FIN_SEGUN',
    # Procedures and functions
    'ESCRIBIR',
    'LEER',
    'PARA',
    'FUNCION',
    'MIENTRAS',
    'SEGUN',
    'DESDE',
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

    'ASIGNAR',
    'IGUAL_A',
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

def t_LOGICO(t):
    r'(VERDADERO|FALSO)'
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

def t_FIN_ALGORITMO(t):
    r'FinAlgoritmo'
    return t

def t_FIN_FUNCION(t):
    r'FinFuncion'
    return t

def t_FIN_PROCEDIMIENTO(t):
    r'FinProcedimiento'
    return t

def t_FIN_SI(t):
    r'FinSi'
    return t

def t_FIN_SI_NO(t):
    r'FinSi_No'
    return t

def t_FIN_MIENTRAS(t):
    r'FinMientras'
    return t

def t_FIN_PARA(t):
    r'FinPara'
    return t

def t_FIN_SEGUN(t):
    r'FinSegun'
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

def t_DESDE(t):
    r'Desde'
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
    r'RETORNAR'
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
    r'ES_MAYOR_QUE'
    return t

def t_ES_MENOR_QUE(t):
    r'ES_MENOR_QUE'
    return t

def t_ES_IGUAL_QUE(t):
    r'ES_IGUAL_QUE'
    return t

def t_ES_MAYOR_O_IGUAL_QUE(t):
    r'ES_MAYOR_O_IGUAL_QUE'
    return t

def t_ES_MENOR_O_IGUAL_QUE(t):
    r'ES_MENOR_O_IGUAL_QUE'
    return t

def t_ES_DISTINTO_QUE(t):
    r'ES_DISTINTO_QUE'
    return t

def t_ASIGNAR(t):
    r'ASIGNAR'
    return t

def t_IGUAL_A(t):
    r'IGUAL_A'
    return t

# Arithmetic Operators
def t_MAS(t):
    r'MAS'
    return t

def t_MENOS(t):
    r'MENOS'
    return t

def t_POR(t):
    r'POR'
    return t

def t_DIVIDIDO(t):
    r'DIVIDIDO'
    return t

def t_ELEVADO_A(t):
    r'ELEVADO_A'
    return t

def t_RESIDUO(t):
    r'RESIDUO'
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
    r'PAR_IZQ'
    return t

def t_PAR_DER(t):
    r'PAR_DER'
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
    r'PUN_Y_COM'
    return t

def t_COMA(t):
    r'COMA'
    return t

def t_DOS_PUN(t):
    r'DOS_PUN'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'A_COM(.*?)C_COM'
    t.value = t.value[len("A_Com"):-len("C_Com")].strip()
    return t

def t_ID(t):
    r'[a-z][_a-z_A-Z_0-9]*'  # Identificadores que comienzan con una letra minúscula
    return t

t_ignore = ' \t'

def t_newlline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_INITIAL_UPPERCASE_ERROR(t):
    r'[A-Z][a-zA-Z_0-9]*'  # Identificadores que comienzan con una letra mayúscula
    #print(f'Error: {t.value} no es un identificador valido., en la linea {t.lineno} y columna {findPosition(t)}.')
    with open('bitacora_De_Errores.html', 'a') as file:
        file.write(f'Error: {t.value} no es un identificador valido, en la linea {t.lineno} y columna {findPosition(t)}.\n')
    t.lexer.skip(1)

def t_error(t):
    #print(f'Error: Caracter inesperado "{t.value[0]}".')
    with open('bitacora_De_Errores.html', 'a') as file:
        file.write(f'<p>Error: Caracter inesperado " {t.value[0]} ", en la linea: {t.lineno}, en la posicion: {findPosition(t)}</p>\n')
    t.lexer.skip(1)

def findPosition(t):
    inicio = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1 # Encontrar la posicion del inicio de la linea
    return (t.lexpos - inicio) + 1 

def getTokens():
    num = 0
    with open('tokens.html', 'w') as file:
        file.write('<html>\n<head>\n<title> Tokens Encontrados </title>\n</head>\n<body>\n')
        file.write('<h1> Tokens Encontrados </h1>\n')
        file.write('<table border="1">\n')
        file.write('<tr><th>Token No.</th><th>Token Encontrado</th><th>Linea</th><th>Posicion</th>\n')
        
        for token in tokensEncontrados:
            num += 1
            file.write(f'<tr><td>{num}</td><td>{token.value}</td><td>{token.lineno}</td><td>{findPosition(token)}</td></tr>\n')
            
        file.write('</table>\n')
        file.write('</body>\n</html>\n')

    print('Se ha creado el archivo tokens.html con los tokens encontrados.')

def readFile(fileName):
    with open(fileName, 'r') as file:
        return file.read()

def test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokensEncontrados.append(tok) # Guardar los tokens encontrados
        #print(tok, f"Linea: {tok.lineno}, en la posicion: {findPosition(tok)}")

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