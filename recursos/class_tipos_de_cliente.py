
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

class Direccion:
    def __init__(self, 
                calle: str, 
                numeroCalle: str, 
                ciudad: str, 
                provincia: str, 
                pais: str):
        self.calle = calle
        self.numeroCalle = numeroCalle
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais


class Cliente(Direccion):
    def __init__(self,
                 calle: str,
                 numeroCalle: str,
                 ciudad: str,
                 provincia: str,
                 pais: str,
                 nombre: str,
                 apellido: str,
                 numeroCliente: str,
                 dni: str):
        super().__init__(calle, 
                        numeroCalle, 
                        ciudad, 
                        provincia, 
                        pais)
        self.nombre = nombre
        self.apellido = apellido
        self.numeroCliente = numeroCliente
        self.dni = dni
    tarjeta_de_credito=None #Sera un bool. Si es False no puede crear tarjetas de credito
    limite_tarjetas_de_credito=None #Si es un bool no puede crear una tarjeta de credito, si es un num entonces ese es el limite
    tarjeta_de_debito=None #Sera un bool. Si es False no puede crear tarjetas de debito
    limite_tarjetas_de_debito=None #Si es un bool no puede crear una tarjeta de debito, si es un num entonces ese es el limite
    chequeras=None #Sera un bool. Si es False no puede tener chequeras
    maximo_chequeras=None #Si es un bool no puede crear tarjetas. Si es un numero, ese es el limite
    maximo_retiro_diario=None #Es un numero, va a ser utilizado como limite a retirar diariamente POR CAJERO
    comision_transferencias=None #Es un escalar entre 1 y 0.99
    maximo_valor_transferencia=None #Es un int. Es el maximo valor que se puede transferir sin solicitar permiso
    cuenta_corriente=None #Al crearse un cliente classic, gold o black, pasa a ser true. Es en pesos.
    cuenta_corriente_descubierto=None #Seria el saldo negativo que puede llegar a tener una cuenta. Si es un bool (false), no puede tener saldo negativo
    caja_de_ahorro_en_dolares=None #Es un bool. Si es False, no puede acceder a las funciones o metodos relacionados con los dolares.
    caja_de_ahorro_en_pesos=None #Es un bool. Si es False, no puede acceder a las funciones o metodos relacionados con los pesos.
    


class ClienteClassic(Cliente):
    def __init__(self, 
                calle: str, 
                numeroCalle: str, 
                ciudad: str, 
                provincia: str, 
                pais: str,
                nombre: str, 
                apellido: str, 
                numeroCliente: str, 
                dni: str):
        super().__init__(calle, 
                        numeroCalle, 
                        ciudad, 
                        provincia, 
                        pais,
                        nombre, 
                        apellido, 
                        numeroCliente, 
                        dni)
    tarjeta_de_credito=False
    limite_tarjetas_de_credito=False
    tarjeta_de_debito=True
    limite_tarjetas_de_debito=1
    chequeras=False
    maximo_chequeras=False
    maximo_retiro_diario=10000
    comision_transferencias=0.99 #Valor transferencia * comision(0.99) = Transferencia - 1%
    maximo_valor_transferencia=150000
    cuenta_corriente=True
    cuenta_corriente_descubierto=False
    caja_de_ahorro_en_dolares=False
    caja_de_ahorro_en_pesos=True
    pass

class ClienteGold(Cliente):
    def __init__(self,
                calle: str,
                numeroCalle: str,
                ciudad: str,
                provincia: str,
                pais: str,
                nombre: str,
                apellido: str,
                numeroCliente: str,
                dni: str):
        super().__init__(calle,
                        numeroCalle,
                        ciudad,
                        provincia,
                        pais,
                        nombre,
                        apellido,
                        numeroCliente,
                        dni)
    tarjeta_de_credito=True
    limite_tarjetas_de_credito=1
    tarjeta_de_debito=True
    limite_tarjetas_de_debito=1
    chequeras=True
    maximo_chequeras=1
    maximo_retiro_diario=20000
    comision_transferencias=0.995 #Valor transferencia * comision(0.995) = Transferencia - 0.5%
    cuenta_corriente=True
    cuenta_corriente_descubierto=10000
    maximo_valor_transferencia=500000
    caja_de_ahorro_dolares=True
    caja_de_ahorro_en_pesos=False
    pass

class ClienteBlack(Cliente):
    def __init__(self,
                 calle: str,
                 numeroCalle: str,
                 ciudad: str,
                 provincia: str,
                 pais: str,
                 nombre: str,
                 apellido: str,
                 numeroCliente: str,
                 dni: str):
        super().__init__(calle,
                        numeroCalle,
                        ciudad,
                        provincia,
                        pais,
                        nombre,
                        apellido,
                        numeroCliente,
                        dni)
    tarjeta_de_credito=True
    limite_tarjetas_de_credito=5
    tarjeta_de_debito=False
    limite_tarjetas_de_debito=False
    chequeras=True
    maximo_chequeras=2
    maximo_retiro_diario=100000
    comision_transferencias=1 #Valor transferencia * comision(1) = Transferencia
    cuenta_corriente=True
    cuenta_corriente_descubierto=10000
    maximo_valor_transferencia=False
    caja_de_ahorro_dolares=True
    caja_de_ahorro_en_pesos=True
    pass