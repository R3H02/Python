# ------ exercicio 3.2 ---------
#receba a nota de um aluno e verificar sua situação acdemica

nota = float(input("Digite sua nota: "))

if nota >= 7 and nota <= 10:
    print("Aprovado")

elif nota >= 5 and nota <= 6.9:
    print("Recuperacao")

elif nota < 5:
    print("Reprovado")

else:
    print("??????")