from xmlrpc.client import boolean
from prueba_cuentas import *
import json
class Cliente():
   


    def __init__(self,nombre,apellido,numero,dni):
        #tipo string todos los parametros
       self.nombre=nombre
       self.apellido=apellido
       self.numero=numero
       self.dni=dni 
    es_black=False
    es_gold=False
    es_classic=False
    

   
   
    @classmethod
    def from_json(cls, args):
        json_dict = json.loads(args)
        return cls(**json_dict)


    def __repr__(self) -> str:
        return f'<{self.nombre} {self.apellido}>'
    


    #por defecto todos los tipos de cuenta comienza en false, si se desea cambiar alguno se debe hacer explicitamente.

    @classmethod
    def ClienteBlack(self):
        
        with open("prueba.json")as f:
            datos=json.load(f)
            print(type(datos))
            for i in datos:
                if i=="tipo":
                    print(datos["tipo"])
                    
                    if datos["tipo"]=="BLACK":
                       Cliente.es_black=True
                       print("agregando propiedades de cliente black")
                       self.tarjeta_de_credito=True
                       self.limite_tarjetas_de_credito=5
                       self.tarjeta_de_debito=True
                       self.limite_tarjetas_de_debito=5 #para probar
                       self.chequeras=True
                       self.maximo_chequeras=2
                       self.maximo_retiro_diario=100000
                       self.comision_transferencias=1 #Valor transferencia * comision(1) = Transferencia
                       self.cuenta_corriente=True
                       self.cuenta_corriente_descubierto=10000
                       self.maximo_valor_transferencia=False
                       self.caja_de_ahorro_en_dolares=True

                       
                     
                     
                    
                    
                    
                    
                    
                    else: 
                          print("usted no es cliente black, usted es un cliente ",datos["tipo"])
                    
   
    @classmethod
    def ClienteClassic(self):
        with open("prueba.json")as f:
            datos=json.load(f)
            #este print es solo si se necesita debugear
            print(type(datos))
            for i in datos:
                if i=="tipo":
                    
                    
                    if datos["tipo"]=="Classic":
                       print("ingresaste al if con exito, generando cliente classic")
                       Cliente.es_classic=True
                    self.tarjeta_de_credito=False
                    self.limite_tarjetas_de_credito=False
                    self.tarjeta_de_debito=True
                    self.limite_tarjetas_de_debito=1
                    self.chequeras=False
                    self.maximo_chequeras=False
                    self.maximo_retiro_diario=10000
                    self.comision_transferencias=0.99 #Valor transferencia * comision(0            self.99) = Transferencia - 1%
                    self.maximo_valor_transferencia=150000
                    self.cuenta_corriente=True
                    self.cuenta_corriente_descubierto=False
                    self.caja_de_ahorro_en_dolares=False
                    self.caja_de_ahorro_en_pesos=True
                      
                       
                    
                    
                    
                    
                    
                else:
                        print("usted no es classic, usted es",datos["tipo"])
    
    @classmethod
    def ClienteGold(self):
        with open("prueba.json")as f:
            datos=json.load(f)
            print(type(datos))
            for i in datos:
                if i=="tipo":
                    
                    
                    if datos["tipo"]=="GOLD":
                       print("ingresaste al if con exito, generando cliente Gold")
                       Cliente.es_gold=True
                       print("Asignando propiedades de cliente gold...")
                 
                       self.tarjeta_de_credito=True
                       self.limite_tarjetas_de_credito=1
                       self.tarjeta_de_debito=True
                       self.limite_tarjetas_de_debito=1
                       self.chequeras=True
                       self.maximo_chequeras=1
                       self.maximo_retiro_diario=20000
                       self.comision_transferencias=0.995 #Valor transferencia * comision(0.995) = Transferencia - 0.5%
                       self.cuenta_corriente=True
                       self.cuenta_corriente_descubierto=10000
                       self.maximo_valor_transferencia=500000
                       self.caja_de_ahorro_en_dolares=True
                       self.caja_de_ahorro_en_pesos=False
                                
                    
                    
                    
                else:
                        
                        print("usted no es gold, usted es",datos["tipo"])
                        break
                        

                 #   if es_black==True:
                   #     print("Beneficios de ser cliente BLACK")

           # print(""" 1) CAJA DE AHORRO EN PESOS Y CUENTA CORRIENTE EN PESOS  
            #         2) CAJA DE AHORRO EN DOLARES   
             #        3) TARJETA DE DEBITO ITBANK Y HASTA 5 TARJETAS DE CREDITO
              #       4) SOLICITUD DE HASTA $100.000 PESOS EN CAJEROS AUTOMATICOS
               #      5) SIN COMISION POR TRANSFERENCIAS 
                #     6) TRANSFERENCIAS EN PESOS SIN LIMITES
                 #    7) DESCUBIERTO DE HASTA $10.000 PESOS """)
            
            #abajo va la logica que asigna los valores en True de lo que un cliente black puede tener.
            # ----->
        

            pass
cliente_prueba=Cliente("El","Bananero","002","85236974")
cliente_prueba.ClienteBlack()
print("Si es verdadero se muestra:",cliente_prueba.es_black)



#LA CLASE DIRECCION NO SE UTILIZA.

    
class Direccion():
    def __init__(self,calle,numero,ciudad,provincia,pais):
        #tipo string todos los parametros
        self.calle=calle
        self.numero=numero
        self.ciudad=ciudad
        self.provincia=provincia
        self.pais=pais
        pass










#///////////////////// CODIGO DE LEO /////////////////////////////
""" class Cliente():
        def __init__(self,
                    numeroCliente:str,
                    nombre:str,
                    apellido:str,
                    dni:str,
                    tipoCliente:str, 
                    direccion:dict, 
                    transacciones:list):
            self.numeroCliente = numeroCliente
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni
            self.tipoCliente = tipoCliente
            self.calle = direccion['calle']
            self.numeroCalle = direccion['numeroCalle']
            self.ciudad = direccion['ciudad']
            self.provincia = direccion['provincia']
            self.pais = direccion['pais']
            self.transacciones = transacciones
            self.tarjeta_de_credito=None #Sera un bool. Si es False no puede crear tarjetas de credito
            self.limite_tarjetas_de_credito=None #Si es un bool no puede crear una tarjeta de credito, si es un num entonces ese es el limite
            self.tarjeta_de_debito=None #Sera un bool. Si es False no puede crear tarjetas de debito
            self.limite_tarjetas_de_debito=None #Si es un bool no puede crear una tarjeta de debito, si es un num entonces ese es el limite
            self.chequeras=None #Sera un bool. Si es False no puede tener chequeras
            self.maximo_chequeras=None #Si es un bool no puede crear tarjetas. Si es un numero, ese es el limite
            self.maximo_retiro_diario=None #Es un numero, va a ser utilizado como limite a retirar diariamente POR CAJERO
            self.comision_transferencias=None #Es un escalar entre 1 y 0.99
            self.maximo_valor_transferencia=None #Es un int. Es el maximo valor que se puede transferir sin solicitar permiso
            self.cuenta_corriente=None #Al crearse un cliente classic, gold o black, pasa a ser true. Es en pesos.
            self.cuenta_corriente_descubierto=None #Seria el saldo negativo que puede llegar a tener una cuenta. Si es un bool (false), no puede tener saldo negativo
            self.caja_de_ahorro_en_dolares=None #Es un bool. Si es False, no puede acceder a las funciones o metodos relacionados con los dolares.
            self.caja_de_ahorro_en_pesos=None #Es un bool. Si es False, no puede acceder a las funciones o metodos relacionados con los pesos."""