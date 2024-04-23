from symbol_1 import Symbol

symbolTable = {}

def insertSymbol(name, type=None, scope=None, visibility=None, role=None, line=None, column=None):
    symbolTable[name] = Symbol(name, type, scope, visibility, role, line, column)

def getSymbol(name):
    return symbolTable.get(name)
