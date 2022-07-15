
# Las clases BLACK, GOLD, CLASSIC deben de compartir
# las mismas variables, pero con distinto valor bool
# Ejemplo:
# ===CLASSIC===
# caja_de_ahorro_en_pesos= True
# caja_de_ahorro_en_dolares= False
# ===BLACK===
# caja_de_ahorro_en_pesos= True
# caja_de_ahorro_en_dolares= True
# Esto es para realizar polimorfismo.
# --> Si los clientes contienen caja de ahorro en dolares == True
# ----> Podran realizar operaciones relacionadas con dicha caja.
# ----> Si no es el caso, intentar utilizar esas operaciones arrojara un error (intencional).
import json
class Cliente():
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
        self.caja_de_ahorro_en_pesos=None #Es un bool. Si es False, no puede acceder a las funciones o metodos relacionados con los pesos.
        if self.tipoCliente== 'BLACK':
            self.tarjeta_de_credito=True
            self.limite_tarjetas_de_credito=5
            self.tarjeta_de_debito=False
            self.limite_tarjetas_de_debito=False
            self.chequeras=True
            self.maximo_chequeras=2
            self.maximo_retiro_diario=100000
            self.comision_transferencias=1 #Valor transferencia * comision(1) = Transferencia
            self.cuenta_corriente=True
            self.cuenta_corriente_descubierto=10000
            self.maximo_valor_transferencia=False
            self.caja_de_ahorro_en_dolares=True
            self.caja_de_ahorro_en_pesos=True
        if self.tipoCliente== 'GOLD':
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
        if self.tipoCliente== 'CLASSIC':
            self.tarjeta_de_credito=False
            self.limite_tarjetas_de_credito=False
            self.tarjeta_de_debito=True
            self.limite_tarjetas_de_debito=1
            self.chequeras=False
            self.maximo_chequeras=False
            self.maximo_retiro_diario=10000
            self.comision_transferencias=0.99 #Valor transferencia * comision(0.99) = Transferencia - 1%
            self.maximo_valor_transferencia=150000
            self.cuenta_corriente=True
            self.cuenta_corriente_descubierto=False
            self.caja_de_ahorro_en_dolares=False
            self.caja_de_ahorro_en_pesos=True
    @classmethod
    def from_json(cls, args):
        json_dict = json.loads(args)
        return cls(**json_dict)


    def __repr__(self) -> str:
        return f'<{self.nombre} {self.apellido}>'