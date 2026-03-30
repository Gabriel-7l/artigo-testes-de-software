from datetime import datetime

PRECOS = {"maçã": 2.0, "banana": 1.5, "laranja": 3.0, "uva": 5.0, "manga": 4.0}
historico_cancelamentos = []

class Pedido:
    def __init__(self, id_pedido, cliente, itens):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.itens = itens  # Lista de dicionários com 'produto' e 'quantidade'
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.status = "ativo"

    def calcular_total(self, precos):
        total = 0
        for item in self.itens:
            total += precos[item['produto']] * item['quantidade']  # ERRO: KeyError se produto não estiver em precos
        return total

    def resumo(self, precos):
        print(f"\n📦 Pedido #{self.id_pedido} | Cliente: {self.cliente} | Data: {self.data}")
        for item in self.itens:
            preco_unit = precos.get(item['produto'], 0)
            print(f"   - {item['produto']}: {item['quantidade']}x R${preco_unit:.2f}")
        print(f"   💰 Total: R${self.calcular_total(precos):.2f} | Status: {self.status}")


def validar_nome(nome):
    if len(nome) < 3 or not nome.isalpha():  # ERRO: isalpha() rejeita nomes com espaço (ex: "Ana Paula")
        print("Erro: Nome inválido!")
        return False
    return True

def validar_quantidade(quantidade):
    if quantidade <= 0:  # ERRO: int() vai lançar ValueError antes disso se o usuário digitar texto
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
        quantidade = int(input(f"Digite a quantidade de {produto}: "))  # ERRO: sem try/except para entrada inválida
        if not validar_quantidade(quantidade):
            continue
        itens.append({"produto": produto, "quantidade": quantidade})
    return Pedido(id_pedido, cliente, itens)

def cancelar_pedido(pedidos):
    id_cancelar = input("Digite o ID do pedido a cancelar: ")
    for p in pedidos:
        if p.id_pedido == id_cancelar and p.status == "ativo":
            p.status = "cancelado"
            historico_cancelamentos.append((p.id_pedido, datetime.now().strftime("%d/%m/%Y %H:%M")))
            print(f"Pedido {p.id_pedido} cancelado.")
            return
    print("Pedido não encontrado ou já cancelado.")  # ERRO: não distingue entre "não existe" e "já cancelado"

def relatorio(pedidos):
    ativos = [p for p in pedidos if p.status == "ativo"]
    cancelados = [p for p in pedidos if p.status == "cancelado"]
    total_geral = sum(p.calcular_total(PRECOS) for p in ativos)  # ERRO: KeyError se produto não estiver em PRECOS

    print(f"\n📊 RELATÓRIO")
    print(f"Pedidos ativos: {len(ativos)} | Cancelados: {len(cancelados)}")
    print(f"Total em aberto: R${total_geral:.2f}")

    if historico_cancelamentos:
        print("\n🗑️ Histórico de cancelamentos:")
        for id_p, data in historico_cancelamentos:
            print(f"   Pedido #{id_p} cancelado em {data}")

def ver_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido registrado.")
        return
    for p in pedidos:
        p.resumo(PRECOS)

def main():
    pedidos = []
    menu = """
1 - Criar pedido
2 - Ver pedidos
3 - Cancelar pedido
4 - Relatório
5 - Sair
Escolha: """

    while True:
        opcao = input(menu)
        if opcao == "1":
            pedido = criar_pedido()
            if pedido:
                pedidos.append(pedido)
                print(f"Pedido {pedido.id_pedido} criado com sucesso.")
        elif opcao == "2":
            ver_pedidos(pedidos)
        elif opcao == "3":
            cancelar_pedido(pedidos)
        elif opcao == "4":
            relatorio(pedidos)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
