
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
# --> Si las clientes contienen caja de ahorro en dolares == True
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
    limite_tarjetas_de_debito=1
    '☑️Solamente una tarjeta de debito'
    '''👆Se crea con el cliente'''
    caja_de_ahorro_pesos=True
    '☑️Solo tiene una caja de ahorro en pesos creada cuando se dio de alta el cliente'
    caja_de_ahorro_dolares=False
    '👆Como no tiene cuenta en dolares NO PUEDE comprar y vender dolares'#!Falta implementar
    maximo_retiro_diario=10000
    '👆Solo puede retirar hasta un maximo de $10.000 diarios por cajero.'#!Falta implementar
    tarjeta_credito=False
    chequeras=False
    '👆No tienen acceso a tarjetas de credito ni chequeras'#!Falta implementar
    comision_transferencias=0.01
    '👆La comision por transferencias hechas es de 1%'#!Falta implementar
    maximo_valor_transferencia=150000
    '👆No puede recibir transferencias mayores a $150.000 sin previo aviso'#!Falta implementar
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
    limite_tarjetas_de_debito=1
    '☑️Solamente una tarjeta de debito'
    '''👆Se crea con el cliente'''
    cuenta_corriente=True
    cuenta_corriente_descubierto=10000
    'Tiene una cuenta corriente con un descubierto de $10.000.'
    '''👆Tener presente que como tiene cuenta corriente,
                 el saldo podria
    ser negativo y hasta -$10.000 si tiene cupo diario para la operacion
    que se quiera realizar'''
    caja_de_ahorro_dolares=True
    'Tiene una caja de ahorro en dolares'
    '''👆Puede comprar en dolares'''
    tarjeta_credito=True
    limite_tarjetas_de_credito=1
    'Puede tener solo una tarjeta de credito'
    maximo_retiro_diario=20000
    'Las extracciones de efectivo tienen un maximo de $20.000 por dia'
    chequeras=True
    'Pueden tener chequera'
    comision_transferencias=0.005
    'La comision por transferencias hechas es de 0.5%'
    'No puede recibir transferencias mayores a $500.000 sin previo aviso'
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
    limite_tarjetas_de_credito=5
    '☑️Pueden tener como maximo 5 tarjetas de credito'
    'Tienen:'
    '''👉 Caja de ahorro en pesos'''
    '''👉 Cuenta corriente en pesos'''
    '''👉 Caja de ahorro en dolares'''
    'Pueden tener descubierto en su cuenta corriente de hasta $10.000'
    'Pueden extraer hasta $100.000 por dia'
    'Pueden tener hasta dos chequeras'
    'No se aplican comisiones a las transferencias'
    'Pueden recibir transferencias por cualquier monto sin previa autorizacion'
    pass