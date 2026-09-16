# ----- exercicio 2.2 -----------
#faça um programa que determine se uma pessoa é aprovada a entrar ou não, as regras são: 12 anos pra cima e uma altura de 1.40m pra cima

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

aprovado = idade >= 12 and altura >= 1.40

if aprovado:
    print("Aprovado")
else:
    print("Negado")
