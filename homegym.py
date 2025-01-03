import random

def gerar_exercicios(dias_academia, idade, altura, peso):
  """
  Gera uma série de exercícios sem impacto de acordo com os dias na academia, 
  idade, altura e peso do usuário.

  Args:
    dias_academia: Número de dias por semana que o usuário vai à academia.
    idade: Idade do usuário em anos.
    altura: Altura do usuário em centímetros.
    peso: Peso do usuário em kg.

  Returns:
    Uma lista de exercícios.
  """

  exercicios = []

  # Exercícios de aquecimento (5 minutos)
  exercicios.append("Aquecimento:")
  exercicios.append("- Caminhada leve (5 minutos)")

  # Exercícios principais (variam com base nos dias na academia)
  exercicios.append("\nExercícios principais:")
  if dias_academia >= 3:
    exercicios.extend([
        "- Agachamento na parede (3 séries de 10-12 repetições)",
        "- Flexões de braço na parede (3 séries de 10-12 repetições)",
        "- Prancha (3 séries de 30-60 segundos)",
        "- Elevação de panturrilhas (3 séries de 15-20 repetições)",
        "- Bicicleta ergométrica (20-30 minutos em ritmo moderado)"
    ])
  else:
    exercicios.extend([
        "- Agachamento na parede (2 séries de 10 repetições)",
        "- Prancha (2 séries de 30 segundos)",
        "- Caminhada (30 minutos em ritmo moderado)"
    ])

  # Exercícios de alongamento (5 minutos)
  exercicios.append("\nAlongamento:")
  exercicios.extend([
      "- Alongamento de panturrilhas",
      "- Alongamento de isquiotibiais",
      "- Alongamento de quadríceps",
      "- Alongamento de peitoral",
      "- Alongamento de costas"
  ])

  # Ajustes com base na idade
  if idade >= 65:
    exercicios.append("\nObservações:")
    exercicios.append(
        "- Se você tiver alguma condição médica pré-existente, consulte um médico antes de iniciar qualquer novo programa de exercícios."
    )
    exercicios.append(
        "- Comece devagar e aumente gradualmente a intensidade e duração dos exercícios."
    )
    exercicios.append("- Use roupas e calçados confortáveis.")
    exercicios.append("- Beba bastante água antes, durante e depois dos exercícios.")
    exercicios.append("- Pare imediatamente se sentir dor.")

  return exercicios


def salvar_exercicios(exercicios, nome_arquivo="exercicios.txt"):
  """
  Salva a lista de exercícios em um arquivo.

  Args:
    exercicios: Lista de exercícios.
    nome_arquivo: Nome do arquivo onde os exercícios serão salvos.
  """

  with open(nome_arquivo, "w") as f:
    for exercicio in exercicios:
      f.write(exercicio + "\n")


if __name__ == "__main__":
  dias_academia = int(input("Quantos dias por semana você irá à academia? "))
  idade = int(input("Qual a sua idade? "))
  altura = float(input("Qual a sua altura em centímetros? "))
  peso = float(input("Qual o seu peso em kg? "))

  exercicios = gerar_exercicios(dias_academia, idade, altura, peso)

  print("\nSua série de exercícios:")
  for exercicio in exercicios:
    print(exercicio)

  salvar_exercicios(exercicios)
  print("\nExercícios salvos em 'exercicios.txt'")
