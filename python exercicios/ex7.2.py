# ------ exercicio 7.2--------


n = int(7)

while True:
    print("tente adivinha qual é o numero")

    r = int(input("NUmero: "))

    if r == 7:
        print("voce acertou!!!!")
        break

    else:
        print("errou, continua tentando")
