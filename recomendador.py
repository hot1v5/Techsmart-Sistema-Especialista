
def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print("Valor inválido. Digite um número maior ou igual a zero.")
            else:
                return valor

        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def ler_opcao(mensagem, opcoes_validas):
    while True:
        opcao = input(mensagem)

        if opcao in opcoes_validas:
            return opcao

        print(
            "Opção inválida. Escolha uma das opções disponíveis."
        )

def coletar_dados():
    print("\n=== TECHSMART INFORMÁTICA ===")
    print("Sistema Especialista de Recomendação de Computadores\n")

    dados = {}

    dados["orcamento"] = ler_float(
    "Qual é o seu orçamento? R$ "
)

    print("\nFinalidade principal:")
    print("1 - Estudos")
    print("2 - Trabalho")
    print("3 - Programação")
    print("4 - Jogos")
    print("5 - Edição de vídeo")
    dados["finalidade"] = ler_opcao(
    "Escolha uma opção: ",
    ["1", "2", "3", "4", "5"]
)

    print("\nNível de jogos:")
    print("1 - Não jogo")
    print("2 - Jogos leves")
    print("3 - Jogos intermediários")
    print("4 - Jogos pesados")
    dados["jogos"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3", "4"]
    )

    print("\nNível de programação:")
    print("1 - Não programo")
    print("2 - Programação básica")
    print("3 - Programação profissional")
    dados["programacao"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3"]
    )

    print("\nNível de edição:")
    print("1 - Não edito")
    print("2 - Edição básica")
    print("3 - Edição profissional")
    dados["edicao"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3"]
    )

    print("\nMultitarefa:")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")
    dados["multitarefa"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3"]
    )

    print("\nResolução desejada para jogos:")
    print("1 - Não se aplica")
    print("2 - Full HD")
    print("3 - 1440p ou superior")
    dados["resolucao"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3"]
    )

    print("\nNecessidade de armazenamento:")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")
    dados["armazenamento"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3"]
    )

    print("\nNecessidade de desempenho:")
    print("1 - Básico")
    print("2 - Intermediário")
    print("3 - Alto")
    dados["desempenho"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3"]
    )

    print("\nVocê usa máquinas virtuais?")
    print("1 - Não")
    print("2 - Sim")
    dados["maquina_virtual"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2"]
    )

    print("\nVocê utiliza ferramentas pesadas de programação, como Android Studio?")
    print("1 - Não")
    print("2 - Sim")
    dados["ferramentas_pesadas"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2"]
    )

    print("\nVocê trabalha com arquivos grandes?")
    print("1 - Não")
    print("2 - Sim")
    dados["arquivos_grandes"] = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2"]
    )

    return dados
    print("\n=== TECHSMART INFORMÁTICA ===")
    print("Sistema Especialista de Recomendação de Computadores\n")

    dados = {}

    dados["orcamento"] = float(
        input("Qual é o seu orçamento? R$ ")
    )

    print("\nFinalidade principal:")
    print("1 - Estudos")
    print("2 - Trabalho")
    print("3 - Programação")
    print("4 - Jogos")
    print("5 - Edição de vídeo")

    dados["finalidade"] = input("Escolha uma opção: ")

    print("\nNível de jogos:")
    print("1 - Não jogo")
    print("2 - Jogos leves")
    print("3 - Jogos intermediários")
    print("4 - Jogos pesados")

    dados["jogos"] = input("Escolha uma opção: ")

    print("\nNível de programação:")
    print("1 - Não programo")
    print("2 - Programação básica")
    print("3 - Programação profissional")

    dados["programacao"] = input("Escolha uma opção: ")

    print("\nNível de edição:")
    print("1 - Não edito")
    print("2 - Edição básica")
    print("3 - Edição profissional")

    dados["edicao"] = input("Escolha uma opção: ")

    print("\nMultitarefa:")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")

    dados["multitarefa"] = input("Escolha uma opção: ")



    return dados

def motor_inferencia(dados):
    recomendacoes_principais = []
    recomendacoes_complementares = []
    regras_ativadas = []

    orcamento = dados["orcamento"]
    finalidade = dados["finalidade"]
    jogos = dados["jogos"]
    programacao = dados["programacao"]
    edicao = dados["edicao"]
    multitarefa = dados["multitarefa"]
    resolucao = dados["resolucao"]
    armazenamento = dados["armazenamento"]
    desempenho = dados["desempenho"]
    maquina_virtual = dados["maquina_virtual"]
    ferramentas_pesadas = dados["ferramentas_pesadas"]
    arquivos_grandes = dados["arquivos_grandes"]

# R01
    if orcamento <= 2500 and finalidade == "1" and jogos == "1":
     recomendacoes_principais.append("Computador básico")
     regras_ativadas.append(
        "R01 - Orçamento até R$ 2.500, uso para estudos e sem jogos."
    )

# R02
    if finalidade == "1" and multitarefa == "1" and edicao == "1" and jogos == "1":
     recomendacoes_principais.append("Computador básico")
     regras_ativadas.append(
        "R02 - Uso para estudos, baixa multitarefa, sem edição e sem jogos."
    )

# R03
    if finalidade == "2" and multitarefa == "1":
     recomendacoes_principais.append("Computador básico")
     regras_ativadas.append(
        "R03 - Uso para trabalho com baixa necessidade de multitarefa."
    )

# R04
    if finalidade == "2" and multitarefa == "3" and orcamento >= 2500:
     recomendacoes_principais.append("Computador intermediário")
     regras_ativadas.append(
        "R04 - Trabalho com alta multitarefa e orçamento compatível."
    )

# R05
    if finalidade == "3" and programacao == "2" and orcamento < 4000:
     recomendacoes_principais.append("Computador intermediário")
     regras_ativadas.append(
        "R05 - Programação básica com orçamento abaixo de R$ 4.000."
    )

# R06
    if finalidade == "3" and programacao == "3" and multitarefa == "3":
     recomendacoes_principais.append("Computador para programação")
     regras_ativadas.append(
        "R06 - Programação profissional com alta multitarefa."
    )

# R07
    if finalidade == "3" and maquina_virtual == "2":
     recomendacoes_complementares.append(
        "Priorizar maior quantidade de memória RAM"
    )
     regras_ativadas.append(
        "R07 - Uso de máquinas virtuais exige maior quantidade de memória RAM."
    )

# R08
    if (
    finalidade == "3"
    and ferramentas_pesadas == "2"
    and multitarefa == "3"
):
     recomendacoes_principais.append(
        "Computador para programação de alto desempenho"
    )
     regras_ativadas.append(
        "R08 - Uso de ferramentas pesadas de desenvolvimento com alta multitarefa."
    )

# R09
    if jogos == "2" and orcamento <= 3000:
     recomendacoes_principais.append("Computador intermediário")
     regras_ativadas.append(
        "R09 - Jogos leves com orçamento de até R$ 3.000."
    )

# R10
    if finalidade == "4" and jogos == "3" and orcamento >= 3500:
     recomendacoes_principais.append("Computador gamer")
     regras_ativadas.append(
        "R10 - Jogos intermediários com orçamento compatível para computador gamer."
    )

# R11
    if finalidade == "4" and jogos == "4" and orcamento >= 4000:
     recomendacoes_principais.append("Computador gamer")
     regras_ativadas.append(
        "R11 - Jogos pesados com orçamento de pelo menos R$ 4.000."
    )

# R12
    if finalidade == "4" and jogos == "4" and desempenho == "3":
     recomendacoes_principais.append(
        "Computador gamer de alto desempenho"
    )
     regras_ativadas.append(
        "R12 - Jogos pesados com necessidade de alto desempenho."
    )

# R13
    if jogos == "4" and resolucao == "2":
     recomendacoes_complementares.append(
        "Priorizar placa de vídeo dedicada"
    )
     regras_ativadas.append(
        "R13 - Jogos pesados em Full HD necessitam de placa de vídeo dedicada."
    )

# R14
    if jogos == "4" and resolucao == "3":
     recomendacoes_complementares.append(
        "Priorizar placa de vídeo de alto desempenho"
    )
     regras_ativadas.append(
        "R14 - Jogos pesados em 1440p ou resolução superior exigem GPU mais potente."
    )

# R15
    if finalidade == "5" and edicao == "2" and orcamento >= 3000:
     recomendacoes_principais.append("Computador intermediário")
     regras_ativadas.append(
        "R15 - Edição básica com orçamento adequado para computador intermediário."
    )

# R16
    if finalidade == "5" and edicao == "3":
     recomendacoes_principais.append(
        "Computador para edição de vídeo"
    )
     regras_ativadas.append(
        "R16 - Edição profissional exige uma configuração específica para criação de conteúdo."
    )

# R17
    if finalidade == "5" and edicao == "3" and desempenho == "3":
     recomendacoes_principais.append(
        "Computador de alto desempenho"
    )
     regras_ativadas.append(
        "R17 - Edição profissional associada à necessidade de alto desempenho."
    )

# R18
    if edicao == "3" and arquivos_grandes == "2":
     recomendacoes_complementares.append(
        "Priorizar SSD de maior capacidade"
    )
     regras_ativadas.append(
        "R18 - Edição profissional com arquivos grandes exige maior capacidade de armazenamento."
    )

# R19
    if armazenamento == "3":
     recomendacoes_complementares.append(
        "SSD de maior capacidade"
    )
     regras_ativadas.append(
        "R19 - O cliente informou alta necessidade de armazenamento."
    )

# R20
    if armazenamento == "3" and (jogos == "4" or edicao == "3"):
     recomendacoes_complementares.append(
        "Armazenamento de 1 TB ou mais"
    )
     regras_ativadas.append(
        "R20 - Jogos pesados ou edição profissional combinados com alto armazenamento."
    )

# R21
    if multitarefa == "3":
     recomendacoes_complementares.append(
        "Priorizar maior quantidade de memória RAM"
    )
     regras_ativadas.append(
        "R21 - Alta multitarefa exige maior quantidade de memória RAM."
    )

# R22
    if orcamento < 2500 and desempenho == "3":
     recomendacoes_principais.append(
        "Orçamento insuficiente para o perfil desejado"
    )
     regras_ativadas.append(
        "R22 - O cliente deseja alto desempenho, mas possui orçamento inferior a R$ 2.500."
    )

# R23
    if 2500 <= orcamento <= 4000 and desempenho == "2":
     recomendacoes_principais.append(
        "Computador intermediário"
    )
     regras_ativadas.append(
        "R23 - Orçamento entre R$ 2.500 e R$ 4.000 com necessidade de desempenho intermediário."
    )

# R24
    if orcamento > 6000 and desempenho == "3":
     recomendacoes_principais.append(
        "Computador de alto desempenho"
    )
     regras_ativadas.append(
        "R24 - Orçamento superior a R$ 6.000 e necessidade de alto desempenho."
    )

# R25
    if finalidade == "3" and jogos == "4" and orcamento >= 5000:
     recomendacoes_principais.append(
        "Computador gamer de alto desempenho adequado também para programação"
    )
     regras_ativadas.append(
        "R25 - O cliente programa, joga títulos pesados e possui orçamento de pelo menos R$ 5.000."
    )

    return (
        recomendacoes_principais,
        recomendacoes_complementares,
        regras_ativadas
    )

def escolher_recomendacao_principal(recomendacoes):
    prioridades = {
        "Computador básico": 1,
        "Computador intermediário": 2,
        "Computador para programação": 3,
        "Computador para edição de vídeo": 3,
        "Computador gamer": 4,
        "Computador para programação de alto desempenho": 5,
        "Computador gamer de alto desempenho": 5,
        "Computador de alto desempenho": 5,
        "Computador gamer de alto desempenho adequado também para programação": 6,
        "Orçamento insuficiente para o perfil desejado": 10
    }

    if not recomendacoes:
        return None

    return max(
        recomendacoes,
        key=lambda item: prioridades.get(item, 0)
    )

if __name__ == "__main__":

    dados_cliente = coletar_dados()

    (
        recomendacoes_principais,
        recomendacoes_complementares,
        regras_ativadas
    ) = motor_inferencia(dados_cliente)

    recomendacoes_principais = list(
        dict.fromkeys(recomendacoes_principais)
    )

    recomendacoes_complementares = list(
        dict.fromkeys(recomendacoes_complementares)
    )

    recomendacao_principal = escolher_recomendacao_principal(
        recomendacoes_principais
    )

    print("\n=== RESULTADO DO SISTEMA ESPECIALISTA ===")

    if recomendacao_principal:
        print("\nRECOMENDAÇÃO PRINCIPAL:")
        print("-", recomendacao_principal)

        if recomendacoes_complementares:
            print("\nRECOMENDAÇÕES COMPLEMENTARES:")

            for item in recomendacoes_complementares:
                print("-", item)

        print("\n=== EXPLICAÇÃO DO RACIOCÍNIO ===")

        for regra in regras_ativadas:
            print("-", regra)

    else:
        print(
            "\nNão foi possível chegar a uma conclusão "
            "com as informações fornecidas."
        )

