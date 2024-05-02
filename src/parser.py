import ply.yacc as yacc

from lexer import tokens, findPosition, test, getTokens
from symbol_table import insertSymbol, getSymbol, printSymbolTableHTML

# Initial rule
def p_programa(p):
    '''
    programa : ALGORITMO cuerpo FIN_ALGORITMO
                | funciones ALGORITMO cuerpo FIN_ALGORITMO
    '''
    if len(p) == 3:
        #p[0] = p[2]
        print(f'{p[1]}, {p[2]} ,{p[3]}')
    else:
        p[0] = p[1], p[2], p[3], p[4]
        print(f'{p[1]}, {p[2]}, {p[3]}, {p[4]}')

def p_cuerpo(p):
    '''
    cuerpo : sentencias
    '''
    p [0] = p[1]

def p_sentencias(p):
    '''
    sentencias : sentencia sentencias
               | sentencia
    '''
    if len(p) == 2: # Si hay mas de una sentencia, DEPENDIENDO LA CANTIDAD DE SIMBOLOS DE LA PRODUCCION
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_sentencia(p):
    '''
    sentencia : posible_declaracion_variable
                | estructura_escribir
                | leer
                | asignaciones
                | para
                | mientras
                | segun
                | multiple_si
                | llamar_funciones
    '''
    p[0] = p[1]
    p.set_lineno(0, p.lineno(1))

def p_posible_declaracion_variable(p):
    '''
    posible_declaracion_variable : declaracion_variable
                                |  multiple_declaracion_variable
    '''
    p[0] = p[1]

def p_declaracion_variable(p):
    '''
    declaracion_variable : DEFINIR ID COMO TIPO_DATO
    '''
    p[0] = ('Definicion', p[2], p[4])
    insertSymbol(p[2], p[4], 'Global', 'Public', 'Variable', p.lineno(1), findPosition(p.slice[2]))

def p_multiple_declaracion_variable(p):
    '''
    multiple_declaracion_variable : DEFINIR ID COMA ID COMO TIPO_DATO
                                | DEFINIR ID COMA ID COMA ID COMO TIPO_DATO
                                | DEFINIR ID COMA ID COMA ID COMA ID COMO TIPO_DATO
                                | DEFINIR ID COMA ID COMA ID COMA ID COMA ID COMO TIPO_DATO
    '''
    if len(p) == 7:
        p[0] = ('Definicion', p[2], p[4], p[6])
        insertSymbol(f"{p[2]}, {p[4]}", p[6], 'Global', 'Public', 'Variable', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}")
    elif len(p) == 9:
        p[0] = ('Definicion', p[2], p[4], p[6], p[8])
        insertSymbol(f"{p[2]}, {p[4]}, {p[6]}", p[8], 'Global', 'Public', 'Variable', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}, {findPosition(p.slice[6])}")
    elif len(p) == 11:
        p[0] = ('Definicion', p[2], p[4], p[6], p[8], p[10])
        insertSymbol(f"{p[2]}, {p[4]}, {p[6]}, {p[8]}", p[10], 'Global', 'Public', 'Variable', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}, {findPosition(p.slice[6])}, {findPosition(p.slice[8])}")
    elif len(p) == 13:
        p[0] = ('Definicion', p[2], p[4], p[6], p[8], p[10], p[12])
        insertSymbol(f"{p[2]}, {p[4]}, {p[6]}, {p[8]}, {p[10]}", p[12], 'Global', 'Public', 'Variable', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}, {findPosition(p.slice[6])}, {findPosition(p.slice[8])}, {findPosition(p.slice[10])}")

def p_asignaciones(p):
    '''
    asignaciones : asignacion
                | asignacion_con_operacion
    '''
    p[0] = p[1]

def p_asignacion(p):
    '''
    asignacion : ID ASIGNAR tipo_dato_identificador
    '''
    p[0] = ('Asignacion', p[1], p[3])

def p_asignacion_con_operacion(p):
    '''
    asignacion_con_operacion : ID ASIGNAR operaciones_matematicas
    '''
    p[0] = ('Asignacion', p[1], p[3])

def p_estructura_escribir(p):
    '''
    estructura_escribir : escribir
                        | escribir_cadena_id
                        | escribir_cadena_id_cadena
                        | escribir_cadena_id_id
    '''
    p[0] = p[1]

def p_escribir(p):
    '''
    escribir : ESCRIBIR CADENA
                | ESCRIBIR ID
                | ESCRIBIR NUMERO
    '''
    insertSymbol(p[2], 'Cadena', None, 'Public', 'Identificador', p.lineno(1), findPosition(p.slice[2]))
    p[0] = ('Escribir', p[2])

def p_escribir_cadena_id(p):
    '''
    escribir_cadena_id : ESCRIBIR CADENA COMA ID
                        | ESCRIBIR ID COMA CADENA
                        | ESCRIBIR ID COMA ID
                        | ESCRIBIR ID COMA NUMERO
                        | ESCRIBIR NUMERO COMA ID
    '''
    insertSymbol(f"{p[2]}, {p[4]}", 'Cadena', None, 'Public', 'Identificador', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}")
    p[0] = ('Escribir', p[2], p[4])

def p_escribir_cadena_id_cadena(p):
    '''
    escribir_cadena_id_cadena : ESCRIBIR CADENA COMA ID COMA CADENA
                                | ESCRIBIR ID COMA CADENA COMA ID
    '''
    insertSymbol(f"{p[2]}, {p[4]}, {p[6]}", 'Cadena', None, 'Public', 'Identificador', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}, {findPosition(p.slice[6])}")
    p[0] = ('Escribir', p[2], p[4], p[6])
        

def p_escribir_cadena_id_id(p):
    '''
    escribir_cadena_id_id : ESCRIBIR CADENA COMA ID COMA CADENA COMA ID
                            | ESCRIBIR ID COMA CADENA COMA ID COMA CADENA
    '''
    insertSymbol(f"{p[2]}, {p[4]}, {p[6]}, {p[8]}", 'Cadena', None, 'Public', 'Identificador', p.lineno(1), f"{findPosition(p.slice[2])}, {findPosition(p.slice[4])}, {findPosition(p.slice[6])}, {findPosition(p.slice[8])}")
    p[0] = ('Escribir', p[2], p[4], p[6], p[8])

def p_leer(p):
    '''
    leer : LEER ID
    '''
    p[0] = ('Leer', p[2])

def p_para(p):
    '''
    para : PARA ID DESDE NUMERO HASTA NUMERO CON_PASO NUMERO HACER sentencias FIN_PARA
    '''
    p[0] = ('Para', p[2], p[4], p[6], p[8])
    insertSymbol(p[2], 'Entero', 'Local', 'Public', 'Variable Procedimiento', p.lineno(1), findPosition(p.slice[2]))

def p_mientras(p):
    '''
    mientras : MIENTRAS expresion_logica HACER sentencias FIN_MIENTRAS
    '''
    p[0] = ('Mientras', p[2], p[4], p[5]) 

def p_expresion_logica(p):
    '''
    expresion_logica : tipo_dato_identificador operador_relacional tipo_dato_identificador
                    | expresion_logica operador_logico expresion_logica
    '''
    p[0] = (p[1], p[2], p[3])

def p_tipo_dato(p):
    '''
    tipo_dato_identificador : ID
                            | NUMERO
                            | CADENA
    '''
    p[0] = p[1]

def p_operador_logico(p):
    '''
    operador_logico : Y
                    | O
                    | NO
    '''
    p[0] = p[1]

def p_operador_relacional(p):
    '''
    operador_relacional : ES_MAYOR_QUE
                        | ES_MENOR_QUE
                        | ES_IGUAL_QUE
                        | ES_MAYOR_O_IGUAL_QUE
                        | ES_MENOR_O_IGUAL_QUE
                        | ES_DISTINTO_QUE
    '''
    p[0] = p[1]

def p_operaciones_matematicas(p):
    '''
    operaciones_matematicas : operacion_matematica
                            | operacion_matematica_parentesis
                            | operacion_matematica_parentesis operacion_matematica
                            | operacion_matematica operaciones_matematicas
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_operacion_matematica(p):
    '''
    operacion_matematica : tipo_dato_identificador operador_aritmetico tipo_dato_identificador
    '''
    p[0] = (p[1], p[2], p[3])

def p_operador_aritmetico(p):
    '''
    operador_aritmetico : MAS
                        | MENOS
                        | POR
                        | DIVIDIDO
                        | ELEVADO_A
                        | RESIDUO
    '''
    p[0] = p[1]

def p_operacion_matematica_parentesis(p):
    '''
    operacion_matematica_parentesis : PAR_IZQ operacion_matematica PAR_DER
                                    | PAR_IZQ operacion_matematica PAR_DER operador_aritmetico tipo_dato_identificador
                                    | PAR_IZQ operacion_matematica_parentesis PAR_DER
    '''
    p[0] = p[2]

def p_segun(p):
    '''
    segun : SEGUN ID HACER casos DE_OTRO_MODO sentencias FIN_SEGUN
    '''
    p[0] = ('Segun', p[2], p[4])

def p_casos(p):
    '''
    casos : caso casos
            | caso
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_caso(p):
    '''
    caso : NUMERO DOS_PUN sentencias
            | CADENA DOS_PUN sentencias
    '''
    p[0] = ('Caso', p[2], p[3])

def p_multiple_si(p):
    '''
    multiple_si : si multiple_si
                | si_no
    '''
    p[0] = p[1]

def p_si(p):
    '''
    si : SI expresion_logica ENTONCES sentencias FIN_SI
    '''
    p[0] = ('Si', p[2], p[4])

def p_si_no(p):
    '''
    si_no : SI expresion_logica ENTONCES sentencias SI_NO sentencias FIN_SI
    '''
    p[0] = ('Si_No', p[2], p[4], p[6])

def p_funciones(p):
    '''
    funciones : funcion funciones
                | funcion 
    '''
    p[0] = p[1]

def p_tipo_retorno_funcion(p):
    '''
    tipo_retorno_funcion : ID
                        | LOGICO
                        | CADENA
    '''
    p[0] = p[1]

def p_funcion(p):
    '''
    funcion : funcion_sin_retorno
            | funcion_con_retorno
            | funcion_con_parametros_con_retorno
    '''
    p[0] = p[1]

def p_funcion_sin_retorno(p):
    '''
    funcion_sin_retorno : FUNCION ID PUN_Y_COM cuerpo FIN_FUNCION
    '''
    p[0] = ('Funcion', p[2], p[4])
    insertSymbol(p[2], 'Funcion', 'Global', 'Public', 'Funcion', p.lineno(1), findPosition(p.slice[2]))

def p_funcion_con_retorno(p):
    '''
    funcion_con_retorno : FUNCION ID PUN_Y_COM cuerpo RETORNAR tipo_retorno_funcion FIN_FUNCION
    '''
    p[0] = ('Funcion', p[2], p[4], p[5], p[6])
    insertSymbol(p[2], 'Funcion', 'Global', 'Public', 'Funcion', p.lineno(1), findPosition(p.slice[2]))

def p_funcion_con_parametros_con_retorno(p):
    '''
    funcion_con_parametros_con_retorno : FUNCION ID PAR_IZQ parametros PAR_DER PUN_Y_COM cuerpo RETORNAR tipo_retorno_funcion FIN_FUNCION
    '''
    p[0] = ('Funcion', p[2], p[4], p[7])
    insertSymbol(p[2], 'Funcion', 'Global', 'Public', 'Funcion', p.lineno(1), findPosition(p.slice[2]))

def p_parametros(p):
    '''
    parametros : ID COMO TIPO_DATO
                | ID COMO TIPO_DATO COMA parametros
    '''
    if len(p) == 4:
        p[0] = ('Parametros', p[1], p[3])
    else:
        p[0] = ('Parametros', p[1], p[3], p[5])

def p_llamar_funciones(p):
    '''
    llamar_funciones : llamar_funcion llamar_funciones
                    | llamar_funcion
    '''
    p[0] = p[1]

def p_llamar_funcion_sin_parametros(p):
    '''
    llamar_funcion : ID PAR_IZQ PAR_DER
    '''
    p[0] = ('Llamar_Funcion', p[1], p[3])

def p_llamar_funcion_con_parametros(p):
    '''
    llamar_funcion : ID PAR_IZQ tipo_dato_identificador PAR_DER
                    | ID PAR_IZQ tipo_dato_identificador COMA tipo_dato_identificador PAR_DER
                    | ID PAR_IZQ tipo_dato_identificador COMA tipo_dato_identificador COMA tipo_dato_identificador PAR_DER
                    | ID PAR_IZQ tipo_dato_identificador COMA tipo_dato_identificador COMA tipo_dato_identificador COMA tipo_dato_identificador PAR_DER
    '''
    if len(p) == 5:
        p[0] = ('Llamar_Funcion', p[1], p[3])
    elif len(p) == 7:
        p[0] = ('Llamar_Funcion', p[1], p[3], p[5])
    elif len(p) == 9:
        p[0] = ('Llamar_Funcion', p[1], p[3], p[5], p[7])
    elif len(p) == 11:
        p[0] = ('Llamar_Funcion', p[1], p[3], p[5], p[7], p[9])

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}")
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f'<p>Error Sintactico: " {p.value} " en la linea: {p.lineno}, y columna: {findPosition(p)}<p/>\n')
        while True:
            tok = parser.token()
            if not tok or tok.type == 'FIN_ALGORITMO':
                break
        parser.restart()
    else:
        print("Syntax error at EOF")
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f'<p>Error Sintactico: " {p.value} " en la linea: {p.lineno}, y columna: {findPosition(p)}<p/>\n')

parser = yacc.yacc()

def parse(data):
    return parser.parse(data)

# Test
if __name__ == '__main__':

    file = 'codigo_fuente.txt'
    with open(file, 'r') as f:
        data = f.read()

    test(data)
    getTokens()

arbolSintactico = parse(data)
#print(arbolSintactico)
printSymbolTableHTML()
