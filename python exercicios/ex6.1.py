# ------ exercicio 6.1 ---------
#faça um programa que pede ao usuario digitar senha, só ira ser encerrado caso ele acerta, utilizando while 

senha = "1234"
s = input("digite a senha: ")

while s != senha:
    print("senha incorreta, tente novamente ")
    s = input("digite a senha: ")
else:
    print("senha correta")
