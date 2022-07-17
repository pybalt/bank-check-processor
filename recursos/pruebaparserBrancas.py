#En este sript estpy probando recorrer el json y mostrar las variables cargadas en diccionario
import json

class Cliente():


    def __init__(self,numeroCliente,nombre,apellido,dni,tipo, direccion):
       self.numeroCliente=numeroCliente
       self.nombre=nombre
       self.apellido=apellido
       self.dni=dni 
       self.tipo=tipo
       self.calle= direccion ['calle']
       self.numeroDireccion= direccion['numeroDireccion']
       self.ciudad=direccion['ciudad']
       self.provincia=direccion['provincia']
       self.pais=direccion['pais']


    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)


    def __repr__(self):
            return f'<Cliente {self.apellido}>'


json_string = '''{
    "numeroCliente": 100001,
    "nombre": "Nicolas",
    "apellido": "Gaston",
    "dni": "29494777",
    "tipo": "BLACK",
    "direccion": {
        "calle": "Rivadavia",
        "numeroDireccion": "7900",
        "ciudad": "Capital Federal",
        "provincia": "Buenos Aires",
        "pais": "Argentina"
    }
    }'''



cli = Cliente.from_json(json_string)
print(cli.dni)
print(cli.provincia)
print(cli.tipo)

if cli.tipo == "BLACK":
    print("Usted es un cliente BLACK y dispone de saldo ilimitado")