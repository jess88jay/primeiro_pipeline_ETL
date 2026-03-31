# Pipeline ETL com Python

Este projeto foi desenvolvido com o objetivo de praticar conceitos básicos de ETL (Extract, Transform, Load) utilizando Python e Pandas.

## Objetivo do projeto

O pipeline realiza a leitura de dois arquivos CSV:

- Um arquivo com o ID e nome dos usuários
- Um arquivo com o ID do usuário e sua renda mensal

Na etapa de transformação, os dados são tratados e unificados em um único arquivo final.

## Etapas do ETL

### Extract
Leitura dos arquivos:
- `users.csv`
- `renda_usuarios.csv`

### Transform
Tratamentos realizados:
- Padronização da coluna `nome` para letras maiúsculas
- Conversão da coluna `renda_mensal` para tipo float
- Junção dos dois arquivos através do ID do usuário
- Remoção da coluna duplicada `id_usuario`

### Load
Geração de um novo arquivo CSV contendo:
- `id`
- `nome`
- `renda_mensal`

