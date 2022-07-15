import json
class Cliente():
   
    def __init__(self,nombre,apellido,numero,dni):
        #tipo string todos los parametros
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni
   
    #por defecto todos los tipos de cuenta comienza en false, si se desea cambiar alguno se debe hacer explicitamente.
  

    es_black=False
    es_gold=False
    es_classic=False
    

    def ClienteBlack(self):
        with open("prueba.json")as f:
            datos=json.load(f)
            print(type(datos))
            for i in datos:
                if i=="tipo":
                    print("Generando cliente",datos["tipo"])
                    es_black=True
                    print(es_black)
        if es_black==True:
            print("Beneficios de ser cliente BLACK")

            print(""" 1) CAJA DE AHORRO EN PESOS Y CUENTA CORRIENTE EN PESOS  
                     2) CAJA DE AHORRO EN DOLARES   
                     3) TARJETA DE DEBITO ITBANK Y HASTA 5 TARJETAS DE CREDITO
                     4) SOLICITUD DE HASTA $100.000 PESOS EN CAJEROS AUTOMATICOS
                     5) SIN COMISION POR TRANSFERENCIAS 
                     6) TRANSFERENCIAS EN PESOS SIN LIMITES
                     7) DESCUBIERTO DE HASTA $10.000 PESOS """)
            #abajo va la logica que asigna los valores en True de lo que un cliente black puede tener.
            # ----->
        

            pass
class Direccion():
    def __init__(self,calle,numero,ciudad,provincia,pais):
        #tipo string todos los parametros
        self.calle=calle
        self.numero=numero
        self.ciudad=ciudad
        self.provincia=provincia
        self.pais=pais
        pass
class Cuenta():
    def __init__(self,limite_extraccion,limite_transferencia,costo_transferencia,monto,saldo_descubierto_disponible):
        #tipo float todos los parametros
        self.limite_extraccion=limite_extraccion
        self.limite_transferencia=limite_transferencia
        self.costo_transferencia=costo_transferencia
        self.monto=monto
        self.saldo_descubierto_disponible=saldo_descubierto_disponible
        pass

cliente_prueba=Cliente("El","Bananero","002","85236974")
cliente_prueba.ClienteBlack()