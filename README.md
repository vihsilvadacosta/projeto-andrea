
# Detecção de Acessos Anômalos com Isolation Forest

Este projeto tem como objetivo demonstrar uma análise automatizada de acessos de usuários a partir de um arquivo de log simulado, utilizando técnicas de aprendizado de máquina para detecção de anomalias.

## 📌 Descrição

Através da biblioteca `Isolation Forest`, identificamos comportamentos suspeitos em sessões de usuários com base na duração das sessões e no número de páginas visitadas. O projeto simula dados, aplica normalização e gera visualizações para auxiliar na interpretação dos resultados.

## 🚀 Funcionalidades

- Simulação de um arquivo de log de acessos de usuários
- Normalização de dados (duração da sessão e páginas visitadas)
- Detecção de anomalias com o algoritmo `Isolation Forest`
- Classificação dos acessos em **Normal** e **Suspeito**
- Geração de alertas para acessos classificados como suspeitos
- Visualização gráfica dos acessos

## 🛠️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/projeto-andrea.git
cd seu-projeto
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

```
├── user_logs.csv              # Arquivo de logs gerado automaticamente
├── main.py                    # Script principal com todo o processamento
├── alertas_criticos.csv       # Arquivo com os acessos suspeitos
├── requirements.txt           # Lista de dependências
├── README.md                  # Este arquivo
└── .gitignore                 # Arquivos ignorados pelo Git
```

## 👨‍💻 Autores

- [Vitória e Suelen]


