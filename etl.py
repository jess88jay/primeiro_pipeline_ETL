import pandas as pd

#Extrair--------------------------------------------------
def extrair_dados(arquivo_entrada):
    df = pd.read_csv(arquivo_entrada)
    return df

#Transformar------------------------------------------------
def padronizar_dados(df_usuarios, df_renda):
    df_usuarios["nome"] = df_usuarios["nome"].str.upper() #padronizar nome para maiúsculo
    df_renda["renda_mensal"] = df_renda["renda_mensal"].astype(float) #padronizar renda para float
    #realizar merge entre os dois arquivos com base no id do usuário
    df_final = pd.merge(
        df_usuarios,
        df_renda,
        left_on="id",
        right_on="id_usuario",
        how="inner"
    )
    #remover a coluna id_usuario para não repetir os dados
    df_final = df_final.drop(columns=["id_usuario"])
    return df_final

#Carregar------------------------------------------------
def carregar_dados(df, arquivo_saida):
    df.to_csv(arquivo_saida, index=False, encoding="utf-8-sig")

#Executar o Pipeline ETL--------------------------------

usuarios = "data/users.csv"
renda = "data/renda_usuarios.csv"
arquivo_saida = "output/usuarios_padronizados.csv"

ex_usuarios = extrair_dados(usuarios)
ex_renda = extrair_dados(renda)
df_transformar = padronizar_dados(ex_usuarios, ex_renda)
carregar_dados(df_transformar, arquivo_saida)


print("ETL executado com sucesso!")

