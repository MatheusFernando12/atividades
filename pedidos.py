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
        