print("--------Calculadora - v2.0---------")

sair = False

while sair == False:

    num1 = input("Digite o primeiro número : ")
    num1 = int(num1)
    operador = input(" Digite o operador (+-/*): ")
    num2 = input("Digite o seguindo número : ")
    num2 = int(num2)

    # + soma
    if operador == "+":
        operacao = num1 + num2

    # - subtração
    if operador == "-":
        operacao = num1 - num2

    # / divisão
    if operador == "/":
        operacao = num1 / num2

    # * multiplicação
    if operador == "*":
        operacao = num1 * num2

    print("Resultado : ")
    print(operacao)

    teste = input("Deseja sair (s/n) : ")
    if teste == "s":
        sair = True
