ARQUIVO = "tarefas.txt"
def carregar_tarefas():

    print("Estoque de frutas\nO que deseja fazer\n")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as file:
            return [linha.strip().split("|") for linha in file.readlines()]
    except FileNotFoundError:
        return[]
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        for tarefa, status in tarefas:
            file.write(f"{tarefa} | {status}\n")

def adicionar_tarefa(tarefas):
    descricao = input("O que deseja alocar no estoque: ")
    descricao1 =tarefas.append([descricao, " ❌ Fora de estoque"])
    salvar_tarefas(tarefas)
    print(f"O produto '{descricao}' alocado com sucesso\n")
def listar_tarefas(tarefas):
    if not tarefas:
        print("nenhum produto encontrado.\n")
    else:
        for i, (descricao, status) in enumerate(tarefas, start=1):
            print(f"{i}. {descricao} - {status}")
        print()
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("digite o número do produto concluída")) -1
        if 0 <= indice < len(tarefas):
            print(f"tarefa '{tarefas[indice][0]}' marcada como concluída e removida!\n")
            descricao1 = tarefas.append([descricao1, " ✔️ Fora de estoque"])
            salvar_tarefas(tarefas)
        else:
            print("número inválido.\n")
    except ValueError:
        print("por favor, digite um número válido.\n")
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("digite o número do produto que deseja excluir: ")) -1 
        if 0 <= indice < len(tarefas):
            print(f"produto '{tarefas[indice][0]}' excluída com sucesso\n")
            del tarefas[indice]
            salvar_tarefas(tarefas)
        else:
            print("número inválido.\n")
    except ValueError:
        print("por favor, digite um número válido.\n")
def main():
    tarefas = carregar_tarefas()

    while True:
        print("1. alocar ao estoque")
        print("2. listar os protudos do estoque")
        print("3. marcar produto do estoque")
        print("4. excluir produto do estoque")
        print("5. sair do estoque")
        escolha = input("escolha uma opção: ")
        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            excluir_tarefa(tarefas)
        else:
            print("Opção inválida. tente novamente.\n")

if __name__ == "__main__":
    main()
