import sys
import os

# Obtener la ruta del directorio padre (src) y agregarlo al PATH
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from parser import parser
