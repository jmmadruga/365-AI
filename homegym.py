def gerar_plano_exercicios(dias_treino, tempo_treino, objetivo, nivel, preferencias, restricoes):
    """
    Gera um plano de exercícios mensal, considerando os dias de treino, tempo disponível, objetivo, nível de condicionamento físico, preferências e restricoes do usuário.

    Args:
        dias_treino: Dias disponíveis para treinar por semana.
        tempo_treino: Tempo disponível para treinar por dia (em minutos).
        objetivo: Objetivo do treino (emagrecer, ganhar massa muscular, manter a forma, etc.).
        nivel: Nível de condicionamento físico atual (iniciante, intermediário, avançado).
        preferencias: Preferências de exercícios (quais tipos de exercícios gosta ou não gosta).
        restricoes: Alguma restrição médica ou lesão que impeça a realização de certos exercícios.

    Returns:
        Um plano de exercícios mensal.
    """

    plano = {}
    exercicios = {
        "pernas": {
            "iniciante": ["Agachamentos", "Lunges", "Elevação de panturrilha"],
            "intermediario": ["Agachamentos búlgaros", "Lunges com salto", "Agachamento pistol"],
            "avancado": ["Agachamento pistol", "Lunges com salto e peso", "Saltos em caixa"]
        },
        "costas": {
            "iniciante": ["Flexões de braço", "Prancha", "Superman"],
            "intermediario": ["Flexões de braço inclinadas", "Prancha com elevação de perna", "Remada invertida"],
            "avancado": ["Flexões de braço com uma mão", "Prancha com elevação de perna e braço", "Muscle-up"]
        },
        "peito": {
            "iniciante": ["Flexões de braço", "Flexões de braço inclinadas"],
            "intermediario": ["Flexões de braço declinadas", "Flexões de braço explosivas"],
            "avancado": ["Flexões de braço com uma mão", "Flexões de braço pliométricas"]
        },
        "ombros": {
            "iniciante": ["Flexões de braço", "Elevações laterais com garrafa de água", "Rotações de ombro"],
            "intermediario": ["Flexões de braço pike", "Elevações frontais com garrafa de água", "Crucifixo invertido"],
            "avancado": ["Parada de mão", "Flexões de braço hindu", "Elevações laterais com isometria"]
        },
        "braços": {
            "iniciante": ["Flexões de braço", "Mergulhos em cadeira", "Rosca direta com garrafa de água"],
            "intermediario": ["Flexões de braço diamante", "Mergulhos em cadeira com elevação de perna", "Rosca concentrada com garrafa de água"],
            "avancado": ["Flexões de braço fechadas", "Mergulhos em barra", "Rosca martelo com garrafa de água"]
        },
        "abdomen": {
            "iniciante": ["Prancha", "Abdominais tradicionais", "Elevação de pernas"],
            "intermediario": ["Prancha lateral", "Abdominais bicicleta", "Elevação de pernas com joelhos flexionados"],
            "avancado": ["Prancha com elevação de perna e braço", "Abdominais dragon flag", "Elevação de pernas tesoura"]
        }
    }

    # Define a ordem dos treinos para cada dia da semana, garantindo pelo menos um dia de descanso entre os treinos de cada grupo muscular
    ordem_treinos = ["pernas", "costas", "peito", "ombros", "braços", "abdomen"]

    # Ajusta o número de séries e repetições de acordo com o nível de condicionamento físico
    series = {"iniciante": 2, "intermediario": 3, "avancado": 4}
    repeticoes = {"iniciante": 10, "intermediario": 12, "avancado": 15}

    # Gera o plano de exercícios para cada dia da semana
    for i in range(dias_treino):
        dia = i + 1
        grupo_muscular = ordem_treinos[i % len(ordem_treinos)]
        plano[f"Dia {dia}"] = []

        # Adiciona exercícios para o grupo muscular do dia
        for exercicio in exercicios[grupo_muscular][nivel]:
            plano[f"Dia {dia}"].append(f"{exercicio} ({series[nivel]} séries de {repeticoes[nivel]} repetições)")

        # Adiciona exercícios para outros grupos musculares, se houver tempo disponível
        if tempo_treino >= 45 and objetivo == "ganhar massa muscular":
            # Adiciona exercícios para um segundo grupo muscular no mesmo dia
            grupo_muscular_secundario = ordem_treinos[(i + 3) % len(ordem_treinos)]  # Seleciona um grupo muscular diferente do principal
            for exercicio in exercicios[grupo_muscular_secundario][nivel]:
                plano[f"Dia {dia}"].append(f"{exercicio} ({series[nivel]} séries de {repeticoes[nivel]} repetições)")

    # Cria um plano mensal repetindo o plano semanal
    plano_mensal = {}
    for semana in range(4):  # 4 semanas em um mês
        for dia, exercicios in plano.items():
            plano_mensal[f"Semana {semana+1}, {dia}"] = exercicios

    return plano_mensal

def salvar_plano_exercicios(plano, nome_arquivo="plano_exercicios.txt"):
    """
    Salva o plano de exercícios em um arquivo txt.

    Args:
        plano: Dicionário contendo o plano de exercícios.
        nome_arquivo: Nome do arquivo onde o plano será salvo.
    """

    with open(nome_arquivo, "w") as f:
        for dia, exercicios in plano.items():
            f.write(f"{dia}:\n")
            for exercicio in exercicios:
                f.write(f"- {exercicio}\n")
            f.write("\n")

if __name__ == "__main__":
    dias_treino = int(input("Quantos dias por semana você pode treinar? "))
    tempo_treino = int(input("Quanto tempo você tem disponível para treinar por dia (em minutos)? "))
    objetivo = input("Qual o seu objetivo com o treino (emagrecer, ganhar massa muscular, manter a forma, etc.)? ")
    nivel = input("Qual o seu nível de condicionamento físico (iniciante, intermediário, avançado)? ")
    preferencias = input("Você tem alguma preferência por tipos de exercícios (ex: prefere exercícios para membros superiores)? ")
    restricoes = input("Você tem alguma restrição médica ou lesão? ")

    plano_exercicios = gerar_plano_exercicios(dias_treino, tempo_treino, objetivo, nivel, preferencias, restricoes)

    print("\nSeu plano de exercícios:")
    for dia, exercicios in plano_exercicios.items():
        print(f"{dia}:")
        for exercicio in exercicios:
            print(f"- {exercicio}")
        print()

    salvar_plano_exercicios(plano_exercicios)
    print("Plano de exercícios salvo em 'plano_exercicios.txt'")
