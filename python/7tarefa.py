# gerenciador de tarefas -manipulação de arquivo
ARQUIVO = "tarefas.txt"

# função para carregar as tarefas
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as file:
            return [linha.strip().split("|") for linha in file.readlines()]
    except FileNotFoundError:
        return[]
# função para salvar as tarefas
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        for tarefa, status in tarefas:
            file.write(f"{tarefa} | {status}\n")

# função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    descricao= input("digite a descrição da tarefa: ")
    tarefas.append([descricao, " ❌ pendente"])
    salvar_tarefas(tarefas)
    print(f"tarefa '{descricao}' adicionada com sucesso\n")

# função para listar todas as tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("nenhuma tarefa encontrada.\n")
    else:
        for i, (descricao, status) in enumerate(tarefas, start=1):
            print(f"{i}. {descricao} - {status}")
        print()

# função para marcar uma tarefa como concluida
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("digite o número da tarefa concluída")) -1
        if 0 <= indice < len(tarefas):
            print(f"tarefa '{tarefas[indice][0]}' marcada como concluída e removida!\n")
            del tarefas[indice] # remove a tarefa autmaticamente
            salvar_tarefas(tarefas)
        else:
            print("número inválido.\n")
    except ValueError:
        print("por favor, digite um número válido.\n")

# função para excluir uma tarefa manualmente 
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("digite o número da tarefa que deseja excluir: ")) -1 
        if 0 <= indice < len(tarefas):
            print(f"tarefa '{tarefas[indice][0]}' excluída com sucesso\n")
            del tarefas[indice]
            salvar_tarefas(tarefas)
        else:
            print("número inválido.\n")
    except ValueError:
        print("por favor, digite um número válido.\n")


# menu principal
def main():
    tarefas = carregar_tarefas()

    while True:
        print("1. adicionar tarefa")
        print("2. listar tarefas")
        print("3. marcar tarefa como concluida")
        print("4. excluir tarefa")
        print("5. sair")
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
