def calcular(a, b, operacao):
    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        if b == 0:
            return "Erro: Divisão por zero não é permitida "
        return a / b
    else:
            return "Erro: Operação inválida "

while True: 
    a = float(input("Digite o primeiro número: " ))
    b = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    resultado = calcular(a, b, operacao)
    print("Resultado:", resultado)

    de_novo = input("Deseja realizar outra operação? (s/n): ")
    if de_novo.lower() != 's':
        break
                     