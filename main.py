from algoritmos.mdc import calcular_mdc
from algoritmos.soma import somar_digitos
from excecoes.erros import EntradaInvalida, OperacaoInvalida

quantidade= int(input())

for _ in range(quantidade):
    entrada= input().split()

    operacao= entrada[0]

    try:
        if operacao == 'M':
            a= int(entrada[1])
            b= int(entrada[2])

            if a <=0 or b <=0:
                raise EntradaInvalida()
            resultado= calcular_mdc(a,b)
            print(f'MDC = {resultado}')

        elif operacao == 'S':
            numero= int(entrada[1])
            if numero < 0:
                raise EntradaInvalida()

            resultado= somar_digitos(numero)

            print(f'SOMA = {resultado}')

        else:
            raise OperacaoInvalida()

    except EntradaInvalida:
        print('ERRO: EntradaInvalida')

    except OperacaoInvalida:
        print('ERRO: OperacaoInvalida')