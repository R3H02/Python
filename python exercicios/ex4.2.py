# ------ exercicio 4.2 ---------
#receba dois numeros e um caracter representando uma operação matematica (+,-,*,/)

num1 = float(input("Digite o primeiro numero: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo numero: "))

match operador:
    case "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado:.2f}")

    case "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado:.2f}")

    case "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado:.2f}")

    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado:.2f}")
        else:
            print("Erro: nao e possivel dividir por zero!")

    case _:
        print("Operador invalido!")
