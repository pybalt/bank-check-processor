#prueba de razon
import json
from clientes import *
class Razon(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
    
    
    #errores por transferencia
    def probar_logica(self):
        with open("prueba.json")as f:
            datos=json.load(f)
            print(type(datos))
            if Cliente.es_black==True:
                for i in datos:
                 if i=="tipo":
                    if datos["tipo"]=="BLACK":
                        print("usted es un cliente black")
                    if i=="tipoTransaccion":
                            if datos["tipoTransaccion"]<(-10000):
                                print("No se puede realizar la operacion, su saldo es menor a 10000")
                    else:
                                print("todo correcto, puede continuar")

cliente_prueba_2=Razon("juancho","panza","002","12345678")      
cliente_prueba_2.probar_logica()