# ted-02-central-recursiva
# Central Recursiva

## Integrantes

- Ana Clara Ribeiro Quixabeira (R.A. 26.1.13720)
- Katariny de Jesus Barreto (R.A. 26.1.13712)

## Descrição do Projeto

A aplicação Central Recursiva realiza operações matemáticas utilizando funções recursivas. O sistema calcula o Máximo Divisor Comum (MDC) entre dois números e a soma dos dígitos de um número, além de tratar entradas inválidas por meio de exceções personalizadas.

## Como Executar

1. Execute o arquivo `main.py`.
2. Informe a quantidade de operações.
3. Digite as operações conforme o formato solicitado.
4. O programa exibirá o resultado de cada operação.

## Módulos Desenvolvidos

### mdc.py
Responsável pelo cálculo recursivo do Máximo Divisor Comum (MDC).

### soma.py
Responsável pelo cálculo recursivo da soma dos dígitos de um número.

### erros.py
Contém as exceções personalizadas utilizadas pelo sistema.

### main.py
Responsável pela leitura das entradas, validações, tratamento de exceções e exibição dos resultados.

## Algoritmos Recursivos

### Cálculo do MDC
O MDC foi implementado utilizando o algoritmo recursivo de Euclides. A função chama a si mesma até que o segundo número seja igual a zero.

### Soma dos Dígitos
A soma dos dígitos foi implementada de forma recursiva. A função soma o último dígito do número e chama a si mesma até que o número seja reduzido a zero.

## Exceções Personalizadas

### EntradaInvalida
Utilizada quando os valores informados não atendem às regras do problema.

### OperacaoInvalida
Utilizada quando a operação informada não é reconhecida pelo sistema.
