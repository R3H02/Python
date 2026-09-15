# ------ exercicio 6.1 ---------


senha = "1234"
s = input("digite a senha: ")

while s != senha:
    print("senha incorreta, tente novamente ")
    s = input("digite a senha: ")
else:
    print("senha correta")
