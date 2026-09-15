# ------ exercicio 7.1---------


while True:
    print("1 - ver saldo")
    print("2 - fazer deposito")
    print("3 - sair")

    opcao = input("digite uma opção: ")

    if opcao == "1":
        print("----aqui esta seu saldo-----")
    elif opcao == "2":
        print("------fazer um deposito-------")
    elif opcao == "3":
        print("-------saindo--------")
        break

    else:
        print("opção invlida")
