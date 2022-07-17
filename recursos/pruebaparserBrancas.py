#En este sript estpy probando recorrer el json y mostrar las variables cargadas en diccionario
from collections import UserString
import json

class Cliente():


    def __init__(self,numeroCliente,nombre,apellido,dni,tipo, direccion, transacciones):
       self.numeroCliente=numeroCliente
       self.nombre=nombre
       self.apellido=apellido
       self.dni=dni 
       self.tipo=tipo
       self.calle= direccion ['calle']
       self.numeroCalle= direccion['numeroCalle']
       self.ciudad=direccion['ciudad']
       self.provincia=direccion['provincia']
       self.pais=direccion['pais']
       self.estado=transacciones['estado']
       self.tipoTransaccion=transacciones['tipoTransaccion']
       self.cuentaNumero=transacciones['cuentaNumero']
       self.cupoDiarioRestante=transacciones['cupoDiarioRestante']
       self.montoTransaccion=transacciones['montoTransaccion']
       self.fecha=transacciones['fecha']
       self.numeroTransaccion=transacciones['numeroTransaccion']
       self.saldoEnCuenta=transacciones['saldoEnCuenta']
       self.totalTarjetasDeCreditoActualmente=transacciones['totalTarjetasDeCreditoActualmente']
       self.totalChequerasActualmente=transacciones['totalChequerasActualmente']


    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)


    def __repr__(self):
            return f'<Cliente {self.tipo}>'



clientes_list = []
with open('recursos\data.json', 'r') as json_file:
    clientes_data = json.loads(json_file.read())
    datos = clientes_data
    datos=datos["resultados"]
    print(datos[1])

    # clientes= datos[0]
    # transacciones = datos[1]

    # for i in datos[1]:
    #     if i == "tipoTransaccion":
    #         print(i)







  





    # for i in clientes_data:
    #  clientes_list.append(Cliente(**i))

     
# print(clientes_list)






# json_string = '''{
#     "numeroCliente": 100001,
#     "nombre": "Nicolas",
#     "apellido": "Gaston",
#     "dni": "29494777",
#     "tipo": "BLACK",
#     "direccion": {
#         "calle": "Rivadavia",
#         "numeroDireccion": "7900",
#         "ciudad": "Capital Federal",
#         "provincia": "Buenos Aires",
#         "pais": "Argentina"
#     }
#     }'''



# cli = Cliente.from_json(json_string)
# print("Numero DNI: " + cli.dni)
# print("Provincia: " + cli.provincia)
# print("Tipo de Cliente: " + cli.tipo)

# if cli.tipo == "BLACK":
#     print("Usted es un cliente BLACK y dispone de saldo ilimitado")