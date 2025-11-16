# 📘 README --- Image Matching

## 📖 Sobre o Projeto

Projeto desenvolvido para conclusão do curso de **Bacharelado em
Engenharia de Software** pela\
**Universidade Católica de Santa Catarina**.

Este trabalho compõe o **Projeto N3 --- Controle de Dados** e tem como
objetivo comparar duas imagens e determinar se representam o mesmo local
usando detecção e correspondência de pontos-chave.

------------------------------------------------------------------------

## ⚙️ Funcionalidades

-   📥 Leitura de duas imagens do disco\
-   🎯 Detecção de keypoints utilizando SIFT\
-   🔗 Cálculo e combinação de correspondências entre pontos chave\
-   🖼️ Geração automática de uma imagem com as correspondências
    desenhadas\
-   🧠 Classificação simples:
    -   **Mesmo local**
    -   **Não é o mesmo local**

------------------------------------------------------------------------

## 📂 Estrutura de Diretórios

``` txt
Matching-Images/
│
├── DataSet/
│   ├── Place1/
│   ├── Place2/
│   ├── Place3/
│   ├── Place4/
│   └── Place5/
│
├── Compare.py
├── ImageMatching.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## 🛠️ Como Instalar

### 1️⃣ Clonar o repositório

``` sh
git clone <URL-do-repositório>
cd Matching-Images
```

### 2️⃣ Criar ambiente virtual (opcional)

``` sh
python -m venv venv
```

### 3️⃣ Ativar o ambiente virtual

**Windows**

``` sh
venv\Scripts\activate
```

**Linux/Mac**

``` sh
source venv/bin/activate
```

### 4️⃣ Instalar dependências

``` sh
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Como Rodar

### 1️⃣ Na pasta **DataSet**, crie uma subpasta com o nome do local:

    DataSet/
     └── Place1/

### 2️⃣ Adicione as duas imagens que serão comparadas com os nomes:

    Imagem1.jpg
    Imagem2.jpg

### 3️⃣ Execute o script principal

``` sh
python Compare.py
```

### 4️⃣ Escolha o *Place* desejado no menu

### 5️⃣ Resultado

O arquivo será salvo dentro da própria pasta escolhida com o nome:

    resultado_comparacao.jpg

------------------------------------------------------------------------
