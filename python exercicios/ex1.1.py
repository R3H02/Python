# ----- exercicio 1.1 -------
#declare um variavel para cada um dos seguintes tipos de dados: string, inteiro, float e booleano. Em seguida, imprima o valor de cada variável na tela.

nome = "Joao"
idade = 25
altura = 1.75
possui_carteira = True

print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", f"{altura:.2f}", "metros")
print("Possui carteira de motorista:", "Verdadeiro" if possui_carteira else "Falso")
