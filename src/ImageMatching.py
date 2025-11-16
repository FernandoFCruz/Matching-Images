import cv2
import numpy as np

def comparar_imagens(img1_path, img2_path, saida_path="resultado.jpg"):
  # Lê imagens em cinza
  img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
  img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

  if img1 is None or img2 is None:
    raise FileNotFoundError("Erro: alguma imagem não foi encontrada")

  sift = cv2.SIFT_create()
  kp1, des1 = sift.detectAndCompute(img1, None)
  kp2, des2 = sift.detectAndCompute(img2, None)

  FLANN_INDEX_KDTREE = 1
  index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
  search_params = dict(checks=50)

  flann = cv2.FlannBasedMatcher(index_params, search_params)

  matches = flann.knnMatch(des1, des2, k=2)

  good_matches = []
  for m, n in matches:
    if m.distance < 0.7 * n.distance:
      good_matches.append(m)

  print(f"Total de matches encontrados: {len(matches)}")
  print(f"Matches bons (aprovados): {len(good_matches)}")

  resultado = cv2.drawMatches(
    img1, kp1,
    img2, kp2,
    good_matches,
    None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
  )

  cv2.imwrite(saida_path, resultado)
  print("Imagem salva em:", saida_path)

  if len(good_matches) >= 15:
    print("✅ Provavelmente é o mesmo local.")
  else:
    print("❌ Provavelmente NÃO é o mesmo local.")

  return len(good_matches)