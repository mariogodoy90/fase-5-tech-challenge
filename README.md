# 🌊 Dashboard Educacional - ONG Passos Mágicos

Este projeto apresenta um **dashboard interativo** desenvolvido em **Streamlit**, focado na análise dos impactos da **ONG Passos Mágicos** no desempenho educacional dos alunos. Ele fornece insights estratégicos com base nos dados coletados entre **2022 e 2024**.

---

## 📌 Funcionalidades

👉 **Visão Geral** – Análise geral dos indicadores educacionais.  
👉 **Evolução do Desempenho** – Monitoramento do progresso dos alunos ao longo do tempo.  
👉 **Engajamento e Notas** – Relação entre participação nas atividades e desempenho acadêmico.  
👉 **Comparação por Categoria** – Desempenho por gênero, escola e fase ideal.  
👉 **Conclusões e Insights** – Recomendações para melhorias na aprendizagem.

---

## 🛠️ Como Acessar o Projeto

O dashboard foi implantado no **Streamlit Cloud**. Para acessar a aplicação, basta clicar no link abaixo:

🔗 [Acessar o Dashboard](https://fase-5-tech-challenge.streamlit.app/)

---

## 💽 Estrutura do Projeto
```bash
projeto/
├── data/                      # Dados brutos e processados
│   ├── PEDE 2024 - DATATHON.xlsx  
├── scripts/                   # Scripts de processamento e visualização
│   ├── data_processing.py      # Funções de limpeza e tratamento de dados
│   ├── visualization.py        # Funções para geração de gráficos
├── main.py                     # Código principal do Streamlit
├── requirements.txt             # Dependências do projeto
├── README.md                    # Documentação do projeto
```

---

## 📈 Estrutura do Dashboard

### 🏠 Visão Geral
📌 **Objetivo:** Fornecer uma análise inicial sobre os principais indicadores educacionais.

📌 **Principais Gráficos:**  
🔹 Evolução do Índice de Desenvolvimento Educacional (INDE)  
🔹 Comparação de desempenho por gênero  
🔹 Escolas com melhor desempenho  

---

### 📈 Evolução do Desempenho
📌 **Objetivo:** Acompanhar o progresso dos alunos e identificar melhorias.

📌 **Principais Gráficos:**  
🔹 Evolução da Defasagem Educacional  
🔹 Evolução do Índice de Ponto de Virada (IPV)  

---

### 📘 Engajamento e Notas
📌 **Objetivo:** Avaliar o impacto do engajamento no desempenho acadêmico.

📌 **Principais Gráficos:**  
🔹 Relação entre lições entregues e notas em Português, Matemática e Inglês  

---

### ⚖️ Comparação por Categoria
📌 **Objetivo:** Comparar o desempenho dos alunos por diferentes categorias educacionais.

📌 **Principais Gráficos:**  
🔹 Distribuição de alunos por Fase Ideal  

---

### 💡 Conclusões e Insights
📌 **Objetivo:** Resumir os principais achados e recomendações estratégicas.

📌 **Insights Destacados:**  
🔹 Aumento contínuo do INDE, indicando melhoria na aprendizagem.  
🔹 Redução da Defasagem Educacional, alunos alcançando o nível ideal.  
🔹 Relação forte entre entrega de lições e desempenho acadêmico.  

📌 **Recomendações:**  
🔹 Fortalecer acompanhamento de alunos com maior defasagem.  
🔹 Incentivar participação em atividades e entrega de lições.  
🔹 Explorar parcerias com escolas para reduzir disparidades.

---

## 👨‍💻 Tecnologias Utilizadas
- **Python** 🐍
- **Streamlit** 📊
- **Pandas** 💑
- **Matplotlib** 📊
