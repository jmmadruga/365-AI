"""Código feito pelo Gemini"""

def comparar_apostas(numeros_sorteados, apostas):
  """Compara as apostas com os números sorteados e retorna o número de acertos de cada aposta."""
  resultados = []
  for aposta in apostas:
    acertos = len(set(numeros_sorteados) & set(aposta))
    resultados.append(acertos)
  return resultados

def main():
  """Função principal do programa."""
  numeros_sorteados_str = input("Digite os números sorteados da Mega Sena, separados por espaço: ")
  numeros_sorteados = [int(num) for num in numeros_sorteados_str.split()]  # Converte para inteiros

  num_apostas = int(input("Digite o número de apostas a serem comparadas: "))

  apostas = []
  for i in range(num_apostas):
    aposta_str = input(f"Digite os números da aposta {i+1}, separados por espaço: ")
    aposta = [int(num) for num in aposta_str.split()]  # Converte para inteiros
    apostas.append(aposta)

  resultados = comparar_apostas(numeros_sorteados, apostas)

  for i, resultado in enumerate(resultados):
    print(f"Aposta {i+1}: {apostas[i]} - Acertos: {resultado}")

if __name__ == "__main__":
  main()
