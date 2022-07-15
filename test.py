import json
from recursos import class_tipos_de_cliente as C
from recursos import class_transaccion as T


Leonel = C.Cliente(100001,
        "Leonel",
        "Bravo",
        "29494777",
        "CLASSIC",
        {
            "calle": "Rivadavia",
            "numeroCalle": "7900",
            "ciudad": "Capital Federal",
            "provincia": "Buenos Aires",
            "pais": "Argentina"
        },
        [
        {
                "estado": "ACEPTADA",
                "tipoTransaccion": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 9000,
                "montoTransaccion": 1000,
                "fecha": "06/06/2022 10:00:55",
                "numeroTransaccion": 1,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 10000,
                "montoTransaccion": 11000,
                "fecha": "06/06/2022 10:10:55",
                "numeroTransaccion": 2,
                "saldoEnCuenta": 10000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 9000,
                "fecha": "06/06/2022 10:22:55",
                "numeroTransaccion": 3,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 9000,
                "fecha": "06/06/2022 10:33:33",
                "numeroTransaccion": 4,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "ALTA_TARJETA_CREDITO",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 9000,
                "fecha": "06/06/2022 12:00:00",
                "numeroTransaccion": 5,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "ALTA_CHEQUERA",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 9000,
                "fecha": "06/06/2022 12:30:55",
                "numeroTransaccion": 6,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "COMPRA_DOLAR",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 9000,
                "fecha": "06/06/2022 12:45:33",
                "numeroTransaccion": 7,
                "saldoEnCuenta": 5000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "RECHAZADA",
                "tipoTransaccion": "TRANSFERENCIA_ENVIADA",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 1000000,
                "fecha": "06/06/2022 13:00:55",
                "numeroTransaccion": 8,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "ACEPTADA",
                "tipoTransaccion": "TRANSFERENCIA_RECIBIDA",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 9000,
                "fecha": "06/06/2022 13:11:15",
                "numeroTransaccion": 9,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            },
            {
                "estado": "ACEPTADA",
                "tipoTransaccion": "TRANSFERENCIA_RECIBIDA",
                "cuentaNumero": 190,
                "cupoDiarioRestante": 3000,
                "montoTransaccion": 200000,
                "fecha": "06/06/2022 16:00:55",
                "numeroTransaccion": 10,
                "saldoEnCuenta": 100000,
                "totalTarjetasDeCreditoActualmente": 5,
                "totalChequerasActualmente": 2
            }
        ])
lista_transacciones = list()
for t in Leonel.transacciones:
    objeto = T.Transaccion(t)
    lista_transacciones.append(objeto)

for tr in lista_transacciones:
    print(type(tr))
    print(tr)
print(lista_transacciones[0].estado)