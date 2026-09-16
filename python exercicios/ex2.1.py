# ----- exercicio 2.1 -----------
#

produtos = ["Café", "Leite", "Pão"]
precos = [5.00, 4.50, 3.00]

print("=== Produtos ===")
print("1 - Café: R$ 5,00")
print("2 - Leite: R$ 4,50")
print("3 - Pão: R$ 3,00")

opcao = int(input("Escolha o produto (1-3): "))

if opcao >= 1 and opcao <= 3:
    produto = produtos[opcao - 1]
    preco = precos[opcao - 1]

    print(f"\nVocê escolheu: {produto}")
    print(f"Preço: R$ {preco:.2f}")

    valor_pago = float(input("Informe o valor pago: R$ "))

    if valor_pago >= preco:
        troco = valor_pago - preco
        print(f"Troco: R$ {troco:.2f}")
    else:
        print("Valor insuficiente!")
else:
    print("Opção inválida!")

