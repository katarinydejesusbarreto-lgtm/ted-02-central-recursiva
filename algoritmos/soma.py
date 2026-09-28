def somar_digitos(numero):
    if numero == 0:
        return 0

    return numero % 10 + somar_digitos(numero//10)
