# Segun el .pdf, los motivos por los cuales la transferencia
# fallo deben estar listados como clases(Exception)

class MontoNegativo():
    def __init__(self, monto, saldo, message="Saldo insuficiente") -> None:
        "Monto y Saldo seran utilizados al invocar el error"
        self.monto = monto
        self.saldo = saldo
        self.message = message
        super().__init__(self.message)

    def __repr__(self) -> str:
        return f'{self.message} se pretende gastar {self.monto} con un saldo de {self.saldo}'

    #* Faltaria implementar este archivo.