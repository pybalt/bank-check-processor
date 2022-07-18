class Transaccion:
    def __init__(self, dict:dict) -> None:
        self.estado = dict['estado']
        self.tipoTransaccion = dict['tipoTransaccion']
        self.cuentaNumero = dict['cuentaNumero']
        self.cupoDiarioRestante = dict['cupoDiarioRestante']
        self.montoTransaccion = dict['montoTransaccion']
        self.fecha = dict['fecha']
        self.numeroTransaccion = dict['numeroTransaccion']
        self.saldoEnCuenta = dict['saldoEnCuenta']
        self.totalTarjetasDeCreditoActualmente = dict['totalTarjetasDeCreditoActualmente']
        self.totalChequerasActualmente = dict['totalChequerasActualmente']
        if dict['avisoTransferencia'] == "True":
            self.avisoTransferencia = True
        else:
            self.avisoTransferencia = False
    def __repr__(self) -> str:
        return f'<Transaccion {self.numeroTransaccion} cuenta {self.cuentaNumero}>'