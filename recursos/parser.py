import json
from .submodulos.class_tipos_de_cliente import *

def parser(path):
    with open (path, 'r') as json_file:
        cliente = json.loads(json_file.read())
        nroReporte = cliente['nroReporte']
        cliente = Cliente(cliente)
    return cliente, nroReporte
