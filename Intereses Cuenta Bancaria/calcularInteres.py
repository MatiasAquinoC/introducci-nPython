def calcular_interes(saldo):
    if saldo < 0:
        raise ValueError("El saldo no puede ser negativo.")
    elif saldo < 10000:
        return saldo * 0.03
    else:
        return saldo * 0.04