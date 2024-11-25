tarefas = {}


def adicionar_tarefa(nome, prioridade='baixa'):
    if nome in tarefas:
        print(f"Tarefa '{nome}' já existe.")
    else:
        tarefas[nome] = {'estado': 'pendente', 'prioridade': prioridade}
        print(f"Tarefa '{nome}' adicionada com prioridade {prioridade}!")


def marcar_concluida(nome):
    if nome in tarefas:
        tarefas[nome]['estado'] = 'concluída'
        print(f"Tarefa '{nome}' marcada como concluída!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")


def remover_tarefa(nome):
    if nome in tarefas:
        del tarefas[nome]
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")


def listar_tarefas():
    if tarefas:
        print("\nLista de todas as tarefas:")
        for nome, dados in tarefas.items():
            print(f"{nome} - Estado: {dados['estado']} | Prioridade: {dados['prioridade']}")
    else:
        print("Nenhuma tarefa cadastrada.")


def listar_pendentes():
    encontrou = False
    print("\nTarefas Pendentes:")
    for nome, dados in tarefas.items():
        if dados['estado'] == 'pendente':
            print(f"{nome} - Prioridade: {dados['prioridade']}")
            encontrou = True
    if not encontrou:
        print("Não há tarefas pendentes.")


def listar_concluidas():
    encontrou = False
    print("\nTarefas Concluídas:")
    for nome, dados in tarefas.items():
        if dados['estado'] == 'concluída':
            print(f"{nome} - Prioridade: {dados['prioridade']}")
            encontrou = True
    if not encontrou:
        print("Não há tarefas concluídas.")


def pesquisar_tarefa(nome):
    if nome in tarefas:
        dados = tarefas[nome]
        print(f"Tarefa '{nome}' encontrada. Estado: {dados['estado']} | Prioridade: {dados['prioridade']}")
    else:
        print(f"Tarefa '{nome}' não encontrada.")


def alterar_prioridade(nome, nova_prioridade):
    if nome in tarefas:
        tarefas[nome]['prioridade'] = nova_prioridade
        print(f"Prioridade da tarefa '{nome}' alterada para {nova_prioridade}.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")


def menu():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Remover Tarefa")
        print("4. Listar Tarefas")
        print("5. Listar Tarefas Pendentes")
        print("6. Listar Tarefas Concluídas")
        print("7. Pesquisar Tarefa")
        print("8. Alterar Prioridade")
        print("9. Sair")
        
        opcao = input("Escolha uma opção (1-9): ")

        if opcao == '1':
            nome = input("Digite o nome da tarefa: ")
            prioridade = input("Digite a prioridade (baixa, média, alta): ").lower()
            if prioridade not in ['baixa', 'média', 'alta']:
                print("Prioridade inválida. Definindo como 'baixa'.")
                prioridade = 'baixa'
            adicionar_tarefa(nome, prioridade)
        elif opcao == '2':
            nome = input("Digite o nome da tarefa a ser marcada como concluída: ")
            marcar_concluida(nome)
        elif opcao == '3':
            nome = input("Digite o nome da tarefa a ser removida: ")
            remover_tarefa(nome)
        elif opcao == '4':
            listar_tarefas()
        elif opcao == '5':
            listar_pendentes()
        elif opcao == '6':
            listar_concluidas()
        elif opcao == '7':
            nome = input("Digite o nome da tarefa a ser pesquisada: ")
            pesquisar_tarefa(nome)
        elif opcao == '8':
            nome = input("Digite o nome da tarefa para alterar a prioridade: ")
            nova_prioridade = input("Digite a nova prioridade (baixa, média, alta): ").lower()
            if nova_prioridade not in ['baixa', 'média', 'alta']:
                print("Prioridade inválida. Alteração não realizada.")
            else:
                alterar_prioridade(nome, nova_prioridade)
        elif opcao == '9':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
