def cadastrar_cliente():

    nome = input("Insira o nome do cliente:")
    telefone = input("Insira o telefone do cliente:")
    endereco = input("Insira o endereço do cliente:")
    return {"nome": nome, "telefone": telefone, "endereco": endereço}

    def cadastrar_produtos():
        produtos = []
        while True?
            produto = input("nome do produto (ou digite 'fim' para encerrar")
            if produto == "fim"
                break
            valor = float(input(f"valor de {produto}: "))
            produtos.append({"nome": produto, "valor": valor})
            return produtos
        
        Seu código está com vários erros de sintaxe e alguns nomes de variáveis inconsistentes. Uma versão corrigida e funcionando seria:

def cadastrar_produtos():
    produtos = []

    while True:
        produto = input("Nome do produto (ou digite 'fim' para encerrar): ")

        if produto.lower() == "fim":
            break

        try:
            valor = float(input(f"Valor de {produto}: R$ "))
        except ValueError:
            print("Digite um valor numérico válido.")
            continue

        produtos.append({
            "nome": produto,
            "valor": valor
        })

    return produtos


def calcular_subtotal(valores):
    subtotal = sum(valores)
    taxa_entrega = 5.0
    total = subtotal + taxa_entrega
    return subtotal, total

def emitir_recibo(cliente, produtos, subtotal, total):print("\n Recibo")
print(f"cliente: (cliente['nome'])")
print(f"Telefone: (cliente['telefone'])")
print(f"Endereço: (cliente[ 'endereco']}")
print("\nProdutos:")
for produto in produtos:
print(f" (produto[ 'nome']): R$ (produto[ 'valor']:, 2f)")
print(f" \nsubtotal: R$ (subtotal: 2f)")
print(f"Taxa de Entrega: R$ 5,00")
print(f"Total a pagar: R$ (total:, 2f)")

cliente = cadastrar_cliente()
produto = cadastrar_produtos()
valores = {p("valores")} for p in produto

