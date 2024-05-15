# validador.py

class ValidadorSemantico:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def obtener_tipo_expresion(self, tipo_expresion):
        if type(tipo_expresion) == float:
            return 'Real'
        elif type(tipo_expresion) == int:
            return 'Entero'
        elif type(tipo_expresion) == str:
            return 'Caracter'
        elif type(tipo_expresion) == bool:
            return 'Verdadero' if tipo_expresion else 'Falso'
        return None

    def verificar_variable(self, variable, tipo_expresion, p, posicion):
        symbol_entry = self.symbol_table.getSymbolFunction(variable)
        if symbol_entry is None:
            symbol_entry = self.symbol_table.getSymbol(variable)

        if symbol_entry:
            tipo_variable = symbol_entry.type
            if tipo_variable == tipo_expresion or (tipo_variable == 'Real' and tipo_expresion == 'Numero') or (tipo_variable == 'Logico' and tipo_expresion in ['Verdadero', 'Falso']):
                return ('Asignacion', variable, tipo_expresion)
            else:
                with open('bitacora_De_Errores.html', 'a') as f:
                    f.write(f"<p>Error Semántico: La variable '{variable}' tiene tipo '{tipo_variable}', pero la expresión tiene tipo '{tipo_expresion}'. en la linea: {p.lineno(1)}, y columna: {posicion}<p/>\n")
        else:
            with open('bitacora_De_Errores.html', 'a') as f:
                f.write(f"<p>Error Semántico: La variable '{variable}' no ha sido declarada previamente. en la linea: {p.lineno(1)}, y columna: {posicion} <p/>\n")
        return None
