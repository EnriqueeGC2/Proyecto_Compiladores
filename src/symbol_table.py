from symbol_1 import Symbol

symbolTable = {}

def insertSymbol(value, type=None, scope=None, visibility=None, role=None, line=None, column=None):
    symbolTable[value] = Symbol(value, type, scope, visibility, role, line, column)

def getSymbol(name):
    return symbolTable.get(name)

def updateSymbol(value, type=None, scope=None, visibility=None, role=None, line=None, column=None):
    symbol = getSymbol(value)
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

def printSymbolTable():
    for name, symbol in symbolTable.items():
        for key, value in symbol.__dict__.items():
            print(f'\t{key}: {value}')

def printSymbolTableHTML():
    with open('tabla_de_simbolos.html', 'w') as file:
        file.write('<html>\n<head>\n<title> Tabla de Simbolos </title>\n</head>\n<body>\n')
        file.write('<h1> Tabla de Simbolos </h1>\n')
        file.write('<table border="1">\n')
        file.write('<tr><th>Token</th><th>Tipo</th><th>Alcance</th><th>Visibilidad</th><th>Rol</th><th>Linea</th><th>Columna</th>\n')
        
        for name, symbol in symbolTable.items():
            file.write(f'<tr><td>{symbol.value}</td><td>{symbol.type}</td><td>{symbol.scope}</td><td>{symbol.visibility}</td><td>{symbol.role}</td><td>{symbol.line}</td><td>{symbol.column}</td></tr>\n')
            
        file.write('</table>\n')
        file.write('</body>\n</html>\n')