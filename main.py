import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scripts.data_processing import load_and_clean_data
from scripts.visualization import (
    plot_inde_evolution, 
    plot_defasagem, 
    plot_ipv_evolution, 
    plot_fase_ideal, 
    plot_engajamento_notas,
    plot_genero,
    plot_top_escolas
)

# Configuração inicial do Dashboard
st.set_page_config(page_title='Painel Educacional - Passos Mágicos', layout='wide')

# Título principal
st.title('📊 Painel Educacional - ONG Passos Mágicos')

# Criar um menu lateral mais intuitivo
menu = st.sidebar.radio("📌 Escolha uma Seção:", [
    "🏠 Visão Geral",
    "📈 Evolução do Desempenho",
    "📘 Engajamento e Notas",
    "⚖️ Comparação por Categoria",
    "💡 Conclusões e Insights"
])

# Carregar e limpar os dados
df_analise, df_licoes = load_and_clean_data("f:/Pós/pos-tech-git/fase-5-tech-challenge/data/PEDE 2024 - DATATHON.xlsx")

# Seção: Visão Geral
if menu == "🏠 Visão Geral":
    st.header("🏠 Visão Geral")
    st.write("Nesta seção, apresentamos uma visão ampla da performance educacional dos alunos, considerando fatores como desempenho médio, participação por gênero e análise das melhores escolas.")
    
    st.subheader("📊 Evolução do Índice de Desenvolvimento Educacional (INDE)")
    st.pyplot(plot_inde_evolution(df_analise))
    
    st.subheader("📊 Comparação de Desempenho por Gênero")
    st.pyplot(plot_genero(df_analise))
    
    st.subheader("🏫 Escolas com Melhores Desempenho")
    st.pyplot(plot_top_escolas(df_analise))

# Seção: Evolução do Desempenho
elif menu == "📈 Evolução do Desempenho":
    st.header("📈 Evolução do Desempenho Acadêmico")
    st.write("Nesta seção, analisamos o progresso educacional dos alunos ao longo dos anos, incluindo métricas de defasagem e fatores que impactam a aprendizagem.")
    
    st.subheader("📉 Evolução da Defasagem Educacional")
    st.write("A defasagem educacional indica o quão distante os alunos estão do nível esperado. O objetivo é reduzir esse número ao longo do tempo.")
    st.pyplot(plot_defasagem(df_analise))
    
    st.subheader("📊 Evolução do Índice de Ponto de Virada (IPV)")
    st.write("O Índice de Ponto de Virada (IPV) mede o momento em que os alunos demonstram melhorias significativas no aprendizado.")
    st.pyplot(plot_ipv_evolution(df_analise))

# Seção: Engajamento e Notas
elif menu == "📘 Engajamento e Notas":
    st.header("📘 Engajamento e Desempenho Acadêmico")
    st.write("Aqui analisamos a relação entre o engajamento dos alunos (lições entregues) e o desempenho acadêmico nas principais disciplinas.")
    
    st.subheader("📊 Impacto do Engajamento no Desempenho Acadêmico")
    st.write("Os alunos que entregam mais lições tendem a ter notas mais altas? Este gráfico explora essa relação.")
    st.pyplot(plot_engajamento_notas(df_licoes))

# Seção: Comparação por Categoria
elif menu == "⚖️ Comparação por Categoria":
    st.header("⚖️ Comparação por Categoria Educacional")
    st.write("Esta seção permite visualizar o desempenho educacional segmentado por diferentes categorias, como fase ideal dos alunos.")
    
    st.subheader("📊 Distribuição dos Alunos por Fase Ideal")
    st.write("A fase ideal representa em qual estágio os alunos deveriam estar dentro do seu percurso educacional. O objetivo é que a maioria esteja na fase correta.")
    st.pyplot(plot_fase_ideal(df_analise))

# Seção: Conclusões e Insights
elif menu == "💡 Conclusões e Insights":
    st.header("💡 Conclusões e Recomendações")
    st.write("Com base na análise dos dados, destacamos os principais insights e recomendações para melhorar a performance dos alunos.")
    
    st.markdown("### 🔍 Principais Insights:")
    st.markdown("- **Aumento contínuo do INDE ao longo dos anos**, sugerindo melhorias no aprendizado.")
    st.markdown("- **A Defasagem Educacional vem reduzindo**, o que indica que os alunos estão alcançando o nível adequado de ensino.")
    st.markdown("- **A relação entre lições entregues e desempenho é forte**, mostrando que o engajamento impacta diretamente no aprendizado.")
    
    st.markdown("### 📢 Recomendações:")
    st.markdown("- Fortalecer estratégias de acompanhamento de alunos com maior defasagem.")
    st.markdown("- Incentivar a entrega de lições como parte do desenvolvimento acadêmico.")
    st.markdown("- Explorar parcerias com instituições para reduzir as disparidades entre escolas.")
