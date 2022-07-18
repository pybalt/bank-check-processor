
def handler(name:str, objCliente:object, listTransacciones:list, nroReporte):
    f = open(f'{name}.html', 'w')
    contentHTML = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte</title>
</head>
<!-- Todos los estilos se han aplicado en linea para evitar cualquier tipo de error al generar el reporte por parte de un mal uso del usuario  -->
<body style="background-color:#FFC300;">
    <section style="display: flex; justify-content: center;">
        <div style="width: 620px; height: 500px; background-color: white; border-radius: 5%;box-shadow: 3px 3px 50px 3px rgb(167, 136, 0);">
            <table style="border-collapse: separate;border-spacing: 10px 5px;position: relative; margin: auto; top: 8%;">
                <tr style="vertical-align: top;height:40px;">
                  <td colspan="2"><strong>Reporte N° {nroReporte}</strong></td>
                  <td ></td>
                  <td><strong>22/07/2022</strong></td>
                </tr>

                <tr>
                    <td>{objCliente.nombre}</td>
                    <td>{objCliente.apellido}</td>
                    <td>{objCliente.dni}</td>
                    <td style="text-align:center;">Black</td>
                </tr>

                <tr>
                    <td>Direccion:</td>
                    <td >{objCliente.calle} {objCliente.numeroCalle}</td>
                    <td style="text-align: right;">Cuenta:</td>
                    <td>{objCliente.numeroCliente}</td>
                </tr>
"""
    for transaccion in listTransacciones:
        texto = f"""
                <tr style="height:40px; color: red;"></strong>
                    <td><strong>Transaccion: {transaccion.numeroTransaccion}</strong></td>
                    <td><strong>{transaccion.estado}</strong></td>
                    <td style="text-align: right;"><strong>Tipo:</strong></td>
                    <td><strong>{transaccion.tipoTransaccion}</strong></td>
                  </tr>


                  <tr>
                    <td>N° Cuenta</td>
                    <td colspan="2">{transaccion.cuentaNumero}</td>
                    <td >Estado: Activa</td>
                </tr>

                <tr>
                    <td>Monto:</td>
                    <td >{transaccion.montoTransaccion}</td>
                    <td >Motivo:</td>
                    <td>{transaccion.razon}
                    </td>
                </tr>

                <tr>
                    <td>Saldo en Cuenta:</td>
                    <td >{transaccion.saldoEnCuenta}</td>
                    <td >Fecha de la Operación:</td>
                    <td>{transaccion.fecha}
                    </td>
                </tr>

                <tr style="height:40px;"></strong>
                    <td colspan="2"><strong>Datos Adicionales</strong></td>
                    
                  </tr>

                  <tr>
                    <td>Limite de Extraccion:</td>
                    <td >{objCliente.maximo_retiro_diario}</td>
                    <td >Resto Extraccion:</td>
                    <td>{transaccion.saldoEnCuenta}</td>
                </tr>
                <tr>
                    <td>Tarjetas de Credito:</td>
                    <td >{transaccion.totalTarjetasDeCreditoActualmente}</td>
                    <td >Chequeras Habilitadas:</td>
                    <td>{transaccion.totalChequerasActualmente}</td>
                </tr>

                <tr>
                    <td>Descubierto:</td>
                    <td>{objCliente.cuenta_corriente_descubierto}</td>
                    <td>Comisión:</td>
                    <td>{100 - objCliente.comision_transferencias*100}%</td>
                </tr>

                <tr>
                    <td>Caja de Ahorro(Pesos):</td>
                    <td>{"Si" if objCliente.caja_de_ahorro_en_pesos else "No"}</td>
                    <td>Transferencia sin Aviso
                    </td>
                    <td>{"Sin limite"if not objCliente.maximo_valor_transferencia else objCliente.maximo_valor_transferencia}</td>
                </tr>

                <tr>
                    <td>Caja de Ahorro(Dolares):</td>
                    <td>{"Si" if objCliente.caja_de_ahorro_en_dolares else "No"}</td>
                    <td>Compra de Dolar
                    </td>
                    <td>{"Si" if objCliente.caja_de_ahorro_en_dolares else "No"}</td>
                </tr>
"""
        contentHTML = contentHTML+texto
    textoFinal = """
                </table>
        </div>
    </section>
</body>
</html>
"""
    contentHTML = contentHTML + textoFinal
    f.write(contentHTML)
    f.close()