README - Image Matching

------------------------------------------------------------------------

SOBRE O PROJETO:

Projeto desenvolvido para conculusão do curso de bacharelado em Engenharia de Software pela Universidade católica de Santa Catarina

Projeto N3 - Controle de Dados

------------------------------------------------------------------------

FUNCIONALIDADES - Leitura de duas imagens do disco - Detecção de
keypoints - Cálculo de correspondências entre os pontos
chave - Geração de uma imagem com as correspondências marcadas -
Classificação simples: “mesmo local” ou “não é o mesmo local”

------------------------------------------------------------------------

## 📂 Estrutura de Diretórios

## Matching-Images/
## ├──DataSet
##      ├── Place1
##      ├── Place2
##      ├── Place3
##      ├── Place4
##      ├── Place5
## ├── Compare.py
## ├── ImageMatching.py
## ├── requirements.txt
## ├── README.md
------------------------------------------------------------------------

COMO INSTALAR

1)  Clonar o repositório git clone cd Matching-Images

2)  Criar ambiente virtual (opcional) python -m venv venv

Ativar: Windows: venv Linux/Mac: source venv/bin/activate

3)  Instalar dependências pip install -r requirements.txt

------------------------------------------------------------------------

COMO RODAR

1)  Dentro da Pasta DataSet crie uma subpasta Place

2) Adicione as duas imagens que quer comparar em formato jpg com os nomes 'Imagem1' e 'Imagem2'

3)  Execute: python Compare.py

4) Selecione o Place Desejado a comparar

4)  O resultado será salvo como resultado_comparacao.jpg dentro da própria pasta Place comparada.