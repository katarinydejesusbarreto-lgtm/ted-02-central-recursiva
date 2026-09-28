def calcular_mdc(a,b):
    if b==0:
        return a

    return calcular_mdc(b,a % b)