# ------ exercicio 4.1 ---------
#escreva u programa que receba um numero de 1 a 7 e imprima o dia da semana correspondente (1=domingo, 2- sabado etc)

d = [
    "domingo",
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado"
]

for i, dia in enumerate(d, start=1):
    print(i, dia)