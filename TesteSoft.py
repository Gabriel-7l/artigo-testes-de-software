class Pedido:
    def __init__(self, id_pedido, cliente, itens):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.itens = itens  # Lista de dicionários com 'produto' e 'quantidade'

    def calcular_total(self, precos):
        total = 0
        for item in self.itens:
            total += precos[item['produto']] * item['quantidade']
        return total

def validar_nome(nome):
    if len(nome) < 3 or not nome.isalpha():
        print("Erro: Nome inválido!")
        return False
    return True

def validar_quantidade(quantidade):
    if quantidade <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
        return False
    return True

def criar_pedido():
    id_pedido = input("Digite o ID do pedido: ")

    cliente = input("Digite o nome do cliente: ")
    if not validar_nome(cliente):
        return None

    itens = []
    while True:
        produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
        if produto.lower() == 'sair':
            break
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        if not validar_quantidade(quantidade):
            continue
        itens.append({"produto": produto, "quantidade": quantidade})

    return Pedido(id_pedido, cliente, itens)

def main():
    precos = {"maçã": 2.0, "banana": 1.5, "laranja": 3.0}
    pedidos = []

    while True:
        opcao = input("1 - Criar pedido\n2 - Ver pedidos\n3 - Sair\nEscolha: ")
        if opcao == "1":
            pedido = criar_pedido()
            if pedido:
                pedidos.append(pedido)
                print(f"Pedido {pedido.id_pedido} criado com sucesso.")
        elif opcao == "2":
            for p in pedidos:
                print(f"Pedido {p.id_pedido} - Cliente: {p.cliente} - Total: {p.calcular_total(precos):.2f}")
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
