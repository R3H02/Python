# ----- exercicio 2.2 -----------

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

aprovado = idade >= 12 and altura >= 1.40

if aprovado:
    print("Aprovado")
else:
    print("Negado")
