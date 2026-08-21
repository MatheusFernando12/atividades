print("== Cadastro de cliente ==")

nome = input("Insira o nome do cliente: ")
telefone = input("Insira o telefone do cliente: ")
endereco = input("Insira o endereço do cliente: ")

print("\n== Produtos do pedido ==")

produtos = []
valores = []

while True:
    produto = input("Nome do produto (ou digite 'fim' para encerrar): ")

    if produto.lower() == "fim":
        break

    valor = float(input("Valor do produto: R$ "))

    produtos.append(produto)
    valores.append(valor)

subtotal = 0.0

for valor in valores:
    subtotal += valor

desconto = float(input("Digite o desconto do cliente em %: "))

subtotal_com_desconto = subtotal - (subtotal * desconto / 100)

frete = 5.0
total = subtotal_com_desconto + frete

print("\n=== RECIBO ===")
print(f"Cliente: {nome}")
print(f"Telefone: {telefone}")
print(f"Endereço: {endereco}")

print("\nProdutos:")

for i in range(len(produtos)):
    print(f"- {produtos[i]} - R$ {valores[i]:.2f}")

print(f"\nSubtotal: R$ {subtotal:.2f}")
print(f"Desconto: {desconto:.2f}%")
print(f"Frete: R$ {frete:.2f}")
print(f"Total: R$ {total:.2f}")
