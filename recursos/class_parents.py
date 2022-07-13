#! Las clases BLACK, GOLD, CLASSIC deben de compartir
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
                 perfil: str,
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
        perfil = perfil.upper()

        if perfil == 'CLASSIC' or perfil == 'GOLD' or perfil == 'BLACK':
            self.perfil = perfil
        else:
            raise TypeError("Perfil inexistente")