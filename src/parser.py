import ply.yacc as yacc

from lexer import tokens, findPosition, getTokens
from symbol_table import SymbolTable

from semantic_analyzer import ValidadorSemantico

symbol_table = SymbolTable()
validador = ValidadorSemantico(symbol_table)
# Initial rule
def p_programa(p):
    '''
    programa : ALGORITMO cuerpo FIN_ALGORITMO
                | funciones ALGORITMO cuerpo FIN_ALGORITMO
    '''
    if len(p) == 3:
        p[0] = p[2]
        #print(f'{p[1]}, {p[2]} ,{p[3]}')
    else:
        p[0] = p[1], p[2], p[3]
        #print(f'{p[1]}, {p[2]}, {p[3]}, {p[4]}')

def p_cuerpo(p):
    '''
    cuerpo : sentencias
    '''
    p[0] = p[1]

def p_sentencias(p):
    '''
    sentencias : sentencia sentencias
               | sentencia
    '''
    if len(p) == 2: # Si hay mas de una sentencia, DEPENDIENDO LA CANTIDAD DE SIMBOLOS DE LA PRODUCCION
        p[0] = [p[1]] # Se guarda en una lista, lista que ocntiene un elemento de la posicion 1
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
    #p.set_lineno(0, p.lineno(1))

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
    symbol_table.insertSymbol(p[2], p[4], 'Local', 'Public', 'Variable (Algoritmo)', p.lineno(1),findPosition(p.slice[2]), len(p[2]))

def p_multiple_declaracion_variable(p):
    '''
    multiple_declaracion_variable : DEFINIR ids COMO TIPO_DATO
    '''
    p[0] = ('Definicion', p[2], p[4])
    posicion = 7
    for var in p[2]:
        symbol_table.insertSymbol(var, p[4], 'Local', 'Public', 'Variable (Algoritmo)', p.lineno(1), (findPosition(p.slice[1]) + posicion), len(var))
        posicion += len(var) + 6

def p_ids(p):
    '''
    ids : ID
        | ID COMA ids
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_estructura_escribir(p):
    '''
    estructura_escribir : ESCRIBIR lista_escribir
    '''
    p[0] = ('Escribir', p[2])

def p_lista_escribir(p):
    '''
    lista_escribir : lista_escribir COMA elemento_escribir
                   | elemento_escribir
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_elemento_escribir(p):
    '''
    elemento_escribir : CADENA
                      | ID
                      | NUMERO
    '''
    p[0] = p[1]

def p_leer(p):
    '''
    leer : LEER ID
    '''
    var = symbol_table.getSymbol(p[2])
    if var:
        p[0] = ('Leer', p[2])
    else:
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f"<p>Error Semántico: La variable '{p[2]}' no ha sido declarada previamente. En la línea: {p.lineno(1)}, posicion: {findPosition(p.slice[2])}.</p>\n")

def p_para(p):
    '''
    para : PARA ID DESDE NUMERO HASTA NUMERO CON_PASO NUMERO HACER sentencias FIN_PARA
    '''
    p[0] = ('Para', p[2], p[4], p[6], p[8])
    symbol_table.insertSymbol(p[2], 'Entero', 'Local', 'Public', 'Variable Temporal', p.lineno(1), findPosition(p.slice[2]), len(p[2]))

def p_mientras(p):
    '''
    mientras : mientras_declaraciones mientras
                | mientras_declaraciones
    '''
    p[0] = p[1]

def p_mientras_declaraciones(p):
    '''
    mientras_declaraciones : mientras_v1
                            | mientras_v2
                            | mientras_v3
    '''
    p[0] = p[1]

def p_mientras_v1(p):
    '''
    mientras_v1 : MIENTRAS expresion_logica HACER sentencias FIN_MIENTRAS
    '''
    p[0] = ('Mientras', p[2], p[4], p[5]) 

def p_mientras_v2(p):
    '''
    mientras_v2 : MIENTRAS expresion_logica HACER sentencias MIENTRAS expresion_logica HACER sentencias FIN_MIENTRAS FIN_MIENTRAS
    '''
    p[0] = ('Mientras', p[2], p[4], p[6], p[8], p[9])

def p_mientras_v3(p):
    '''
    mientras_v3 : MIENTRAS LOGICO HACER sentencias FIN_MIENTRAS 
    '''
    #LOGICO = VERDADERO | FALSO
    p[0] = ('Mientras', p[2], p[4], p[5])

def p_asignaciones(p):
    '''
    asignaciones : asignacion asignaciones
                | asignacion
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_asignacion(p):
    '''
    asignacion : asignacion_v1
                | asignacion_con_operacion 
    '''
    p[0] = p[1]

def p_asignacion_v1(p):
    '''
    asignacion_v1 : ID ASIGNAR tipo_dato_identificador
    '''
    #p[0] = ('Asignacion', p[1], p[3])
    variable = p[1]
    tipo_expresion = p[3] 
    tipo_expresion = validador.obtener_tipo_expresion(tipo_expresion)
    try:
        resultado = validador.verificar_variable(variable, tipo_expresion, p, posicion=findPosition(p.slice[1]))
        if resultado:
            p[0] = resultado
    except Exception as e:
        print(e)

def p_asignacion_con_operacion(p):
    '''
    asignacion_con_operacion : ID ASIGNAR operaciones_matematicas
    '''
    id = symbol_table.getSymbol(p[1])
    if id:
        p[0] = ('Asignacion', p[1], p[3])
    else:
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f"<p>Error Semántico: La variable '{p[1]}' no ha sido declarada previamente. En la línea: {p.lineno(1)}, posicion: {findPosition(p.slice[1])}.</p>\n")

def p_expresion_logica(p):
    '''
    expresion_logica : tipo_dato_identificador operador_relacional tipo_dato_identificador
                    | expresion_logica operador_logico expresion_logica
    '''
    p[0] = (p[1], p[2], p[3])

def p_tipo_dato_identificador(p):
    '''
    tipo_dato_identificador : ID
                            | NUMERO
                            | CADENA
                            | REAL
                            | LOGICO
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
    operaciones_matematicas : operacion_matematica_v1
                            | operacion_matematica_v2
    '''
    p[0] = p[1]

def p_operacion_matematica_v1(p):
    '''
    operacion_matematica_v1 : tipo_dato_identificador operador_aritmetico tipo_dato_identificador
    '''
    symbol1 = symbol_table.getSymbol(p[1])
    symbol2 = symbol_table.getSymbol(p[3])

    # Verificar si p[1] es una variable en la tabla de símbolos
    if symbol1:
        # Si p[3] es un entero, permitir la operación si p[1] es numérico
        if isinstance(p[3], int) and symbol1.type in ['Entero', 'Real']:
            p[0] = ('Operacion Matematica', p[1], p[2], p[3])
            return  # Salir de la función después de permitir la operación
        # Si p[3] es una variable, verificar si p[1] y p[3] son compatibles
        elif symbol2 and symbol1.type == symbol2.type:
            p[0] = ('Operacion Matematica', p[1], p[2], p[3])
            return  # Salir de la función después de permitir la operación
        else:
            # Registro de error semántico si los tipos no son compatibles
            with open('bitacora_De_Errores.html', 'a') as f:
                f.write(f"<p>Error Semántico: No se puede realizar la operación matemática entre '{p[1]}' y '{p[3]}' en la línea: {p.lineno(1)}.</p>\n")
            return
    # Si p[1] no es una variable, aplicar la regla original
    if (isinstance(p[1], (int, float)) and isinstance(p[3], (int, float))) or isinstance(p[1], str) and isinstance(p[3], str):
        p[0] = ('Operacion Matematica',p[1], p[2], p[3])
    else:
        # Registro de error semántico si los tipos no son compatibles
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f"<p>Error Semántico: No se puede realizar la operación matemática entre '{p[1]}' y '{p[3]}' en la línea: {p.lineno(1)}.</p>\n")

def p_operacion_matematica_v2(p):
    '''
    operacion_matematica_v2 : tipo_dato_identificador operador_aritmetico tipo_dato_identificador operador_aritmetico tipo_dato_identificador
    '''
    symbol1 = symbol_table.getSymbol(p[1])
    symbol2 = symbol_table.getSymbol(p[3])
    symbol3 = symbol_table.getSymbol(p[5])

    # Verificar si p[1] es una variable en la tabla de símbolos
    if symbol1:
        # Si p[3] es un entero, permitir la operación si p[1] es numérico
        if isinstance(p[3], int) and symbol1.type in ['Entero', 'Real']:
            p[0] = ('Operacion Matematica', p[1], p[2], p[3], p[4], p[5])
            return  # Salir de la función después de permitir la operación
        # Si p[3] es una variable, verificar si p[1] y p[3] son compatibles
        elif symbol2 and symbol1.type == symbol2.type:
            p[0] = ('Operacion Matematica', p[1], p[2], p[3], p[4], p[5])
            return  # Salir de la función después de permitir la operación
        else:
            # Registro de error semántico si los tipos no son compatibles
            with open('bitacora_De_Errores.html', 'a') as f:
                f.write(f"<p>Error Semántico: No se puede realizar la operación matemática entre '{p[1]}' y '{p[3]}' en la línea: {p.lineno(1)}.</p>\n")
            return
    # Si p[1] no es una variable, aplicar la regla original
    if (isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)) and isinstance(p[5], (int, float))) or isinstance(p[1], str) and isinstance(p[3], str) and isinstance(p[5], str):
        p[0] = ('Operacion Matematica',p[1], p[2], p[3], p[4], p[5])
    else:
        # Registro de error semántico si los tipos no son compatibles
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f"<p>Error Semántico: No se puede realizar la operación matemática entre '{p[1]}' y '{p[3]}' en la línea: {p.lineno(1)}.</p>\n")

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

# HACER REGLAS PARA LAS OPERACIONES MATEMATICAS, QUE PERMITA EL INGRESO DE PARENTESIS Y DEMAS

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

#FUNCIONES 
def p_cuerpo_funcion(p):
    '''
    cuerpo_funcion : sentencias_funcion
    '''
    p[0] = p[1]

def p_sentencias_funcion(p):
    '''
    sentencias_funcion : sentencia_funcion sentencias_funcion
                        | sentencia_funcion
    '''
    if len(p) == 2: # Si hay mas de una sentencia, DEPENDIENDO LA CANTIDAD DE SIMBOLOS DE LA PRODUCCION
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_sentencia_funcion(p):
    '''
    sentencia_funcion : posible_declaracion_variable_funcion
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
    #p.set_lineno(0, p.lineno(1))

def p_posible_declaracion_variable_funcion(p):
    '''
    posible_declaracion_variable_funcion : declaracion_variable_funcion
                                        |  multiple_declaracion_variable_funcion
    '''
    p[0] = p[1]

def p_declaracion_variable_funcion(p):
    '''
    declaracion_variable_funcion : DEFINIR ID COMO TIPO_DATO
    '''
    p[0] = ('Definicion', p[2], p[4])
    symbol_table.insertSymbolFunction(p[2], p[4], 'Local', 'Public', 'Variable (Funcion)', p.lineno(1),findPosition(p.slice[2]), len(p[2]))

def p_multiple_declaracion_variable_funcion(p):
    '''
    multiple_declaracion_variable_funcion : DEFINIR ids COMO TIPO_DATO
    '''
    p[0] = ('Definicion', p[2], p[4])
    posicion = 7
    for var in p[2]:
        symbol_table.insertSymbolFunction(var, p[4], 'Local', 'Public', 'Variable (Funcion)', p.lineno(1), (findPosition(p.slice[1]) + posicion), len(var))
        posicion += len(var) + 6
    
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
    funcion_sin_retorno : FUNCION ID PUN_Y_COM cuerpo_funcion FIN_FUNCION
    '''
    p[0] = ('Funcion', p[2], p[4])
    symbol_table.insertSymbol(p[2], 'Funcion', 'Global', 'Public', 'Nombre Funcion', p.lineno(1), findPosition(p.slice[2]), len(p[2]))

def p_funcion_con_retorno(p):
    '''
    funcion_con_retorno : FUNCION ID PUN_Y_COM cuerpo_funcion RETORNAR tipo_retorno_funcion FIN_FUNCION
    '''
    p[0] = ('Funcion', p[2], p[4], p[5], p[6])
    symbol_table.insertSymbol(p[2], 'Funcion', 'Global', 'Public', 'Nombre Funcion', p.lineno(1), findPosition(p.slice[2]), len(p[2]))

def p_funcion_con_parametros_con_retorno(p):
    '''
    funcion_con_parametros_con_retorno : FUNCION ID PAR_IZQ parametros PAR_DER PUN_Y_COM cuerpo_funcion RETORNAR tipo_retorno_funcion FIN_FUNCION
    '''
    p[0] = ('Funcion', p[2], p[4], p[7])
    symbol_table.insertSymbol(p[2], 'Funcion', 'Global', 'Public', 'Nombre Funcion', p.lineno(1), findPosition(p.slice[2]), len(p[2]))

def p_parametros(p):
    '''
    parametros : ID
                | ID COMA parametros
    '''
    if len(p) == 4:
        p[0] = ('Parametros', p[1])
    else:
        p[0] = ('Parametros', p[1], p[3])

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
    var = symbol_table.getSymbol(p[1])
    if var:
        p[0] = ('Llamar_Funcion', p[1])
    else:   
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f"<p>Error Semántico: La función '{p[1]}' no ha sido declarada previamente. En la línea: {p.lineno(1)}, posicion: {findPosition(p.slice[1])}.</p>\n")

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


def contar_lineas_hasta_posicion(texto, posicion):
    # Contador de líneas
    num_lineas = 1
    # Iterar sobre el texto hasta la posición del error
    for i in range(posicion):
        if texto[i] == '\n':
            num_lineas += 1
    return num_lineas

def p_error(p):
    if p:
        numLinea = contar_lineas_hasta_posicion(p.lexer.lexdata, p.lexpos)
        print(f"Syntax error at line {numLinea}")
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f'<p>Error Sintactico: " {p.value} " en la linea: {numLinea}, y columna: {findPosition(p)}<p/>\n')
    else:
        print("Syntax error at EOF")
        with open('bitacora_De_Errores.html', 'a') as f:
            f.write(f'<p>Error de sintaxis: la instruccion esta incorrecta o incompleta.<p/>\n')

parser = yacc.yacc()

def parse(data):
    return parser.parse(data)

def prueba():
    print("Hola")

# Test
if __name__ == '__main__':

    file = 'codigo_fuente.txt'
    with open(file, 'r') as f:
        data = f.read()

    """ test(data)
    getTokens() """

    arbolSintactico = parse(data)
    print(arbolSintactico)
    symbol_table.printSymbolTableHTML()
    getTokens()

    
