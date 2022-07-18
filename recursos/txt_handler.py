from datetime import datetime
import time

def log(NROREPORTE, CLIENTE, TRANSACCIONES):
    file= open('logger.txt', 'w')
    content =f'NRO CLIENTE: {CLIENTE.numeroCliente}\nNROREPORTE: {NROREPORTE}\n'
    for transaccion in TRANSACCIONES:
            actual_time = datetime.now()
            content = content + f'[{actual_time}]:       {transaccion.estado}\n{transaccion.razon}\n'
    file.write(content)
    file.close()
    