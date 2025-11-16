import os
from ImageMatching import comparar_imagens

def executar_comparacao():
  print("\n=== Comparador de Imagens ===\n")

  place = input("Informe o local a comparar: ").strip()

  img1 = "../DataSet/Place"+place+"/imagem1.jpg"
  img2 = "../DataSet/Place"+place+"/imagem2.jpg"

  if not os.path.isfile(img1):
    print("Erro: imagem 1 não encontrada.")
    return
  if not os.path.isfile(img2):
    print("Erro: imagem 2 não encontrada.")
    return

  print("\nProcessando...\n")
  comparar_imagens(img1, img2, "../DataSet/Place"+place+"/resultado_comparacao.jpg")
  print("\n✔ Concluído! Resultado salvo como: resultado_comparacao.jpg\n")

if __name__ == "__main__":
  executar_comparacao()
