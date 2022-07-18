# Las razones no son necesariamente errores, asi que
# tienen su clase definida pero no como exceptions

from .errores.class_errores import MontoNegativo

def analisisTransaccion(objCliente, objTransaccion):
    tipoCl = objCliente.tipoCliente
    match objTransaccion.tipoTransaccion:
        case 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
            if objCliente.maximo_retiro_diario < objTransaccion.montoTransaccion:
                "El monto del retiro no puede superar el max retiro diario"
                MOTIVO = f'FUERA DE LIMITES.\nLIMITE DIARIO: {objCliente.maximo_retiro_diario}\n'
            elif objTransaccion.montoTransaccion > objTransaccion.saldoEnCuenta:
                "El monto del retiro no puede dejar el saldo de la cuenta en negativo"
                MOTIVO = f'SALDO INSUFICIENTE.\nSALDO RESTANTE: {objTransaccion.saldoEnCuenta}\n'
            elif objTransaccion.montoTransaccion > objTransaccion.cupoDiarioRestante:
                "El monto del retiro no puede superar al cupo diario restante"
                MOTIVO = f'CUPO DIARIO INSUFICIENTE.\nCUPO RESTANTE: {objTransaccion.cupoDiarioRestante}\n'
        case 'ALTA_TARJETA_CREDITO':
            if not objCliente.tarjeta_de_credito:
                "La cuenta debe tener permitido tener tj de credito"
                MOTIVO = f'FUERA DE LIMITES.\nUSTED NO PUEDE POSEER TARJETAS DE CREDITO'
            elif objTransaccion.totalTarjetasDeCreditoActualmente == objCliente.limite_tarjetas_de_credito:
                "El numero de tarjetas de credito debe ser menor o igual al limite que permite la cuenta"
                MOTIVO = f'FUERA DE LIMITES.\nLIMITE DE TARJETAS DE CREDITO: {objCliente.limite_tarjetas_de_credito}\n'
        case 'ALTA_CHEQUERA':
            "La cuenta debe tener permitido tener chequeras"
            if not objCliente.chequeras:
                MOTIVO = f'FUERA DE LIMITES.\nUSTED NO PUEDE POSEER CHEQUERAS'
            elif objTransaccion.totalChequerasActualmente == objCliente.maximo_chequeras:
                "El numero de chequeras debe ser menor o igual al limite que permite la cuenta"
                MOTIVO = f'FUERA DE LIMITES.\nLIMITE DE CHEQUERAS: {objCliente.maximo_chequeras}\n'
        case 'COMPRA_DOLAR':
            if not objCliente.caja_de_ahorro_en_dolares:
                "La cuenta debe tener caja de ahorro en dolares"
                MOTIVO = f'FUERA DE LIMITES.\nUSTED NO PUEDE REALIZAR OPERACIONES CON DOLARES'
            elif objTransaccion.montoTransaccion > objTransaccion.saldoEnCuenta:
                "El monto de la transaccion no puede superar al saldo en cuenta"
                MOTIVO = f'SALDO INSUFICIENTE.\nSALDO RESTANTE: {objTransaccion.saldoEnCuenta}\n'
            elif objTransaccion.montoTransaccion > objTransaccion.cupoDiarioRestante:
                "El monto de la transaccion no puede superar al cupo diario restante"
                MOTIVO = f'CUPO DIARIO INSUFICIENTE.\nCUPO RESTANTE: {objTransaccion.cupoDiarioRestante}\n'
            pass
        case 'TRANSFERENCIA_ENVIADA':
            "Primero verificar si tiene descubierto"
            if objCliente.cuenta_corriente_descubierto:
                maximoValor = objTransaccion.saldoEnCuenta + objCliente.cuenta_corriente_descubierto
            else:
                maximoValor = objTransaccion.saldoEnCuenta

            if objTransaccion.montoTransaccion > maximoValor:
                MOTIVO = f'FONDOS INSUFICIENTES.\nFONDOS: {maximoValor}\n'
                "El monto de la transferencia no puede dejar la cuenta en negativo con el descubierto incluido"
            elif not objTransaccion.avisoTransferencia:
                if objCliente.maximo_valor_transferencia:
                    if objTransaccion.montoTransaccion > objCliente.maximo_valor_transferencia:
                        MOTIVO = f'FUERA DE LIMITES.\nUSTED NO PUEDE TRANSFERIR MAS DE {objCliente.maximo_valor_transferencia}\n'
            "Se debe verificar si se aviso el monto de la transferencia"
            "-->Si se aviso, entonces cualquier cantidad es recibida"
            "-->Si no se aviso, la transferencia no puede superar al limite de transferencia sin aviso"
        case 'TRANSFERENCIA_RECIBIDA':
            if not objTransaccion.avisoTransferencia:
                if objCliente.maximo_valor_transferencia:
                    if objTransaccion.montoTransaccion > objCliente.maximo_valor_transferencia:
                        MOTIVO = f'FUERA DE LIMITES.\nUSTED NO PUEDE TRANSFERIR MAS DE {objCliente.maximo_valor_transferencia}\n'
            "Se debe verificar si se aviso el monto de la transferencia"
            "-->Si se aviso, entonces cualquier cantidad es recibida"
            "-->Si no se aviso, la transferencia no puede superar al limite de transferencia sin aviso"
        case _:
            MOTIVO = 'TRANSACCION NO RECONOCIDA'
            #* Realmente, esto solamente existe para contener erores de tipeo.
    return MOTIVO

class Razon:
    def __init__(self, cliente, transaccion) -> None:
        self.transaccion = transaccion
        self.cliente = cliente
        self.razon = analisisTransaccion(cliente, transaccion)
    
    def __repr__(self) -> str:
        return f'{self.razon}'