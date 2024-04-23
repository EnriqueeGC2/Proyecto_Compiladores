import sys
import os
import unittest
# Obtener la ruta del directorio padre (src) y agregarlo al PATH
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from lexer import lexer, getTokens, test, tokensEncontrados

if __name__ == '__main__':

    file = 'codigo_fuente.txt'
    with open(file, 'r') as f:
        data = f.read()

    test(data)
    getTokens()

