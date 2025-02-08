import pandas as pd

def load_and_clean_data(file_path):
    """
    Carrega os dados do arquivo Excel e realiza a limpeza inicial.
    """
    xls = pd.ExcelFile(file_path)
    
    df_pede2022 = xls.parse('PEDE2022')
    df_pede2023 = xls.parse('PEDE2023')
    df_pede2024 = xls.parse('PEDE2024')
    df_licoes = xls.parse('Lições entregues')
    
    # Normalizar colunas para facilitar análise
    def normalize_df(df):
        return df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))
    
    df_pede2022 = normalize_df(df_pede2022)
    df_pede2023 = normalize_df(df_pede2023)
    df_pede2024 = normalize_df(df_pede2024)
    df_licoes = normalize_df(df_licoes)
   
    # Criar DataFrame consolidado para análise de desempenho ao longo dos anos
    df_pede2022['ano'] = 2022
    df_pede2023['ano'] = 2023
    df_pede2024['ano'] = 2024

    # Selecionar colunas importantes
    df_analise = pd.concat([
        df_pede2022[['ra', 'gênero', 'instituição_de_ensino', 'matem', 'portug', 'inglês', 'defas', 'ano', 'inde_22', 'ipv', 'ian', 'fase_ideal']].rename(columns={'metem': 'matemática', 'portug': 'português', 'inglês': 'inglês', 'ipv': 'ipv_score', 'ian': 'ian_score', 'inde_22': 'inde', 'defas': 'defasagem', 'fase_ideal': 'fase_ideal_score'}),
        df_pede2023[['ra', 'gênero', 'instituição_de_ensino', 'mat', 'por', 'ing', 'defasagem', 'ano', 'inde_2023', 'ipv', 'ian', 'fase_ideal']].rename(columns={'mat': 'matemática', 'por': 'português', 'ing': 'inglês', 'ipv': 'ipv_score', 'ian': 'ian_score', 'inde_2023': 'inde', 'fase_ideal': 'fase_ideal_score'}),
        df_pede2024[['ra', 'gênero', 'instituição_de_ensino', 'mat', 'por', 'ing', 'defasagem', 'ano', 'inde_2024', 'ipv', 'ian', 'fase_ideal']].rename(columns={'mat': 'matemática', 'por': 'português', 'ing': 'inglês', 'ipv': 'ipv_score', 'ian': 'ian_score', 'inde_2024': 'inde', 'fase_ideal': 'fase_ideal_score'})
    ], ignore_index=True)

    # Padronizar valores da coluna 'gênero'
    df_analise['gênero'] = df_analise['gênero'].replace({
        'Menina': 'Feminino',
        'Menino': 'Masculino',
        'Feminio': 'Feminino',
        'Masculino': 'Masculino'
    })

    # Normalizar valores da coluna 'instituição_de_ensino'
    df_analise['instituição_de_ensino'] = df_analise['instituição_de_ensino'].replace({
        'Escola Pública': 'Escola Pública',
        'Rede Decisão': 'Privada',
        'Escola JP II': 'Privada',
        'Privada - Programa de Apadrinhamento': 'Privada - Programa de Apadrinhamento',
        'Privada - Programa de apadrinhamento': 'Privada - Programa de Apadrinhamento',
        'Privada *Parcerias com Bolsa 100%': 'Privada - Parcerias com Bolsa 100%',
        'Privada - Pagamento por *Empresa Parceira': 'Privada - Pagamento por Empresa Parceira',
        'Concluiu o 3º EM': 'Concluiu o 3º EM',
        'Nenhuma das opções acima': 'Nenhuma das opções acima',
        'nan': 'Nenhuma das opções acima'
    })

    # Converter colunas numéricas
    df_analise['ipv_score'] = pd.to_numeric(df_analise['ipv_score'], errors='coerce')
    df_analise['ian_score'] = pd.to_numeric(df_analise['ian_score'], errors='coerce')

    print(df_analise.head())
    print(df_licoes.head())
    
    return df_analise, df_licoes