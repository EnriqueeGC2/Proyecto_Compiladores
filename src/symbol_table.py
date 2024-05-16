from symbol_1 import Symbol

class SymbolTable:
    def __init__(self):
        self.symbolTable = {}
        self.symbolTableFunctions = {}

    def insertSymbol(self, value, type=None, scope=None, visibility=None, role=None, line=None, column=None, size=None):
        if value in self.symbolTable:
        # Verificar si ya existe una entrada con el mismo ámbito y rol   
        #print(f'Error semántico: El símbolo {value} ya ha sido declarado en el ámbito {existingSymbol.scope} con rol {existingSymbol.role}.')
            with open('bitacora_De_Errores.html', 'a') as file:
                file.write(f'Error semántico: El símbolo {value} ya ha sido declarado. En la linea {line}, posicion {column}\n')
            return
        else:
        # Si el símbolo no está en la tabla de símbolos, lo agregamos como una nueva entrada
            self.symbolTable[value] = Symbol(value, type, scope, visibility, role, line, column, size)

    def getSymbol(self, name):
        return self.symbolTable.get(name)

    def updateSymbol(self, value, type=None, scope=None, visibility=None, role=None, line=None, column=None, size=None):
        symbol = self.getSymbol(value)
        if symbol:
            if type:
                symbol.type = type
            if scope:
                symbol.scope = scope
            if visibility:
                symbol.visibility = visibility
            if role:
                symbol.role = role
            if line:
                symbol.line = line
            if column:
                symbol.column = column
            if size:
                symbol.size = size
        else:
            # Manejar el caso en el que el símbolo no existe
            pass

    def insertSymbolFunction(self, value, type=None, scope=None, visibility=None, role=None, line=None, column=None, size=None):
        if value in self.symbolTableFunctions:
            # Verificar si ya existe una entrada con el mismo ámbito y rol   
            #print(f'Error semántico: El símbolo {value} ya ha sido declarado en el ámbito {existingSymbol.scope} con rol {existingSymbol.role}.')
            with open('bitacora_De_Errores.html', 'a') as file:
                file.write(f'Error semántico: El símbolo {value} ya ha sido declarada. En la linea {line}, posicion {column}\n')
            return
        else:
            # Si el símbolo no está en la tabla de símbolos, lo agregamos como una nueva entrada
            self.symbolTableFunctions[value] = Symbol(value, type, scope, visibility, role, line, column, size)

    def getSymbolFunction(self, name):
        return self.symbolTableFunctions.get(name)
    
    def updateSymbolFunction(self, value, type=None, scope=None, visibility=None, role=None, line=None, column=None, size=None):
        symbol = self.getSymbolFunction(value)
        if symbol:
            if type:
                symbol.type = type
            if scope:
                symbol.scope = scope
            if visibility:
                symbol.visibility = visibility
            if role:
                symbol.role = role
            if line:
                symbol.line = line
            if column:
                symbol.column = column
            if size:
                symbol.size = size
        else:
            # Manejar el caso en el que el símbolo no existe
            pass

    def print_symbol_table_function(self):
        for name, symbol in self.symbolTableFunctions.items():
            for key, value in symbol.__dict__.items():
                print(f'\t{key}: {value}')        

    def print_symbol_table(self):
        for name, symbol in self.symbolTable.items():
            for key, value in symbol.__dict__.items():
                print(f'\t{key}: {value}')

    def printSymbolTableHTML(self):
        with open('tabla_de_simbolos.html', 'w') as file:
            file.write('<html>\n<head>\n<title> Tabla de Simbolos </title>\n</head>\n<body>\n')
            file.write('<h1> Tabla de Simbolos </h1>\n')
            file.write('<table border="1">\n')
            file.write('<tr><th>Token</th><th>Tipo</th><th>Alcance</th><th>Visibilidad</th><th>Rol</th><th>Linea</th><th>Columna</th><th>Tamaño</th>\n')

            for name, symbol in self.symbolTableFunctions.items():
                file.write(f'<tr><td>{symbol.value}</td><td>{symbol.type}</td><td>{symbol.scope}</td><td>{symbol.visibility}</td><td>{symbol.role}</td><td>{symbol.line}</td><td>{symbol.column}</td><td>{symbol.size}</td></tr>\n')

            for name, symbol in self.symbolTable.items():
                file.write(f'<tr><td>{symbol.value}</td><td>{symbol.type}</td><td>{symbol.scope}</td><td>{symbol.visibility}</td><td>{symbol.role}</td><td>{symbol.line}</td><td>{symbol.column}</td><td>{symbol.size}</td></tr>\n')

            file.write('</table>\n')
            file.write('</body>\n</html>\n')
