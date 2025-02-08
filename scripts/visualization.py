import matplotlib.pyplot as plt
import pandas as pd

def plot_inde_evolution(df_analise):
    """
    Gera o gráfico da evolução do Índice de Desenvolvimento Educacional (INDE) ao longo dos anos.
    """
    # Convert 'inde' column to numeric, ignoring non-numeric values
    df_analise['inde'] = pd.to_numeric(df_analise['inde'], errors='coerce')
    
    df_inde = df_analise.groupby('ano')['inde'].mean().reset_index()
    
    fig, ax = plt.subplots()
    ax.plot(df_inde['ano'], df_inde['inde'], marker='o', linestyle='-')
    ax.set_xlabel("Ano")
    ax.set_ylabel("INDE Médio")
    ax.set_title("Evolução do INDE (2022-2024)")
    ax.set_xticks([2022, 2023, 2024])
    ax.grid(True)
    
    return fig

def plot_defasagem(df_analise):
    """
    Gera o gráfico da evolução da Defasagem Educacional ao longo dos anos.
    """
    # Calcular a média da defasagem para cada ano
    defasagem_media_por_ano = df_analise.groupby('ano')['defasagem'].mean().reset_index()

    # Criar o DataFrame com os anos e as defasagens médias
    df_defasagem = pd.DataFrame({
        'Ano': defasagem_media_por_ano['ano'],
        'Defasagem Média': defasagem_media_por_ano['defasagem']
    })
    
    fig, ax = plt.subplots()
    ax.plot(df_defasagem['Ano'], df_defasagem['Defasagem Média'], marker='o', linestyle='-')
    ax.set_xlabel("Ano")
    ax.set_ylabel("Defasagem Média")
    ax.set_title("Média da Defasagem Educacional (2022-2024)")
    ax.set_xticks([2022, 2023, 2024])
    ax.grid(True)
    
    return fig

def plot_ipv_evolution(df_analise):
    """
    Gera o gráfico da evolução do Índice de Ponto de Virada (IPV) ao longo dos anos.
    """
    # Calcular a média do IPV para cada ano
    ipv_media_por_ano = df_analise.groupby('ano')['ipv_score'].mean().reset_index()

    # Criar o DataFrame com os anos e os IPV médios
    df_ipv = pd.DataFrame({
        'Ano': ipv_media_por_ano['ano'],
        'IPV Médio': ipv_media_por_ano['ipv_score']
    })
    
    fig, ax = plt.subplots()
    ax.plot(df_ipv['Ano'], df_ipv['IPV Médio'], marker='o', linestyle='-')
    ax.set_xlabel("Ano")
    ax.set_ylabel("IPV Médio")
    ax.set_title("Evolução do Índice de Ponto de Virada (IPV) (2022-2024)")
    ax.set_xticks([2022, 2023, 2024])
    ax.grid(True)
    
    return fig

def plot_fase_ideal(df_analise):
    """
    Gera gráfico da distribuição de alunos por fase ideal ao longo dos anos.
    """
    # Selecionar colunas relevantes e padronizar nomes
    df_fase_ideal = df_analise[['ano', 'fase_ideal_score']].dropna()

    # Agrupar e contar os valores por ano e fase ideal
    fase_ideal_counts = df_fase_ideal.groupby(['ano', 'fase_ideal_score']).size().unstack().fillna(0)

    fig, ax = plt.subplots(figsize=(12, 6))
    fase_ideal_counts.plot(kind='bar', stacked=True, ax=ax, colormap="viridis")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Número de Alunos")
    ax.set_title("Distribuição dos Alunos por Fase Ideal ao Longo dos Anos")
    ax.legend(title="Fase Ideal", bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_xticks(range(len(fase_ideal_counts.index)))
    ax.set_xticklabels(fase_ideal_counts.index, rotation=0)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    return fig

def plot_engajamento_notas(df_licoes):
    """
    Gera gráfico da relação entre lições entregues e desempenho dos alunos.
    """
    df_licoes_filtered = df_licoes[['matemática', 'português', 'inglês', 'média']].dropna()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df_licoes_filtered['média'], df_licoes_filtered['matemática'], alpha=0.5, label="Matemática")
    ax.scatter(df_licoes_filtered['média'], df_licoes_filtered['português'], alpha=0.5, label="Português")
    ax.scatter(df_licoes_filtered['média'], df_licoes_filtered['inglês'], alpha=0.5, label="Inglês")
    ax.set_xlabel("Média das Lições Entregues")
    ax.set_ylabel("Nota Média")
    ax.set_title("Relação entre Lições Entregues e Notas")
    ax.legend()
    ax.grid(True)
    
    return fig

def plot_genero(df_analise):
    """
    Gera gráfico de comparação de desempenho por gênero (média do IPV).
    """
    df_genero = df_analise[['gênero', 'ipv_score']].dropna()
    
    fig, ax = plt.subplots(figsize=(8, 5))
    df_genero.groupby('gênero').mean(numeric_only=True)['ipv_score'].plot(kind='bar', color=['blue', 'pink'], ax=ax)
    ax.set_title("Comparação do Índice de Ponto de Virada (IPV) por Gênero")
    ax.set_xlabel("Gênero")
    ax.set_ylabel("Média do IPV")
    ax.set_xticks(range(len(df_genero['gênero'].unique())))
    ax.set_xticklabels(df_genero['gênero'].unique(), rotation=0)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    return fig

def plot_top_escolas(df_analise):
    """
    Gera gráfico de comparação de desempenho por instituição de ensino (média do IPV).
    """
    df_escolas = df_analise[['instituição_de_ensino', 'ipv_score']].dropna()

    # Selecionar as top 10 instituições com mais alunos
    top_escolas = df_escolas['instituição_de_ensino'].value_counts().head(10).index
    df_escolas_filtered = df_escolas[df_escolas['instituição_de_ensino'].isin(top_escolas)]

    fig, ax = plt.subplots(figsize=(12, 5))
    df_escolas_filtered.groupby('instituição_de_ensino').mean(numeric_only=True)['ipv_score'].sort_values().plot(kind='barh', color='green', ax=ax)
    ax.set_title("Média do Índice de Ponto de Virada (IPV) por Instituição de Ensino (Top 10)")
    ax.set_xlabel("Média do IPV")
    ax.set_ylabel("Instituição de Ensino")
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    
    return fig