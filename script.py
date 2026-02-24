import pandas as pd
import numpy as np

data = pd.read_csv('vendas_raw.csv')
df = pd.DataFrame(data)

# Tratamento de Nulos

df['preco_unitario'] = df['preco_unitario'].fillna(df['valor_total'] / df['quantidade'])
df['cliente'] = df['cliente'].fillna('Não Identificado')
df['categoria'] = df['categoria'].fillna('Outros')

# Anonimização de e-mails

def mascarar_email(email):
    if pd.isnull(email):
        return email
    partes = email.split('@')
    if len(partes) != 2:
        return email
    nome_usuario = partes[0]
    dominio = partes[1]
    nome_usuario_mascarado = nome_usuario[:2] + '****' + nome_usuario[-1] if len(nome_usuario) > 3 else '****'
    return f"{nome_usuario_mascarado}@{dominio}"

df['email_cliente'] = df['email_cliente'].apply(mascarar_email)

# Padronização de Datas

df['data_venda'] = df['data_venda'].astype(str).str.strip()
datas_convertidas = pd.to_datetime(df['data_venda'], dayfirst=True, format='mixed', errors='coerce')
df['data_venda'] = datas_convertidas.dt.strftime('%Y-%m-%d')
df['data_venda'] = df['data_venda'].fillna('Data não informada')

# Normalização de Categorias

df['categoria'] = df['categoria'].str.strip().str.title()

df.to_csv('vendas_cleaned.csv', index=False)

from sqlalchemy import create_engine

usuario = 'root' 
senha = '*'
host = 'localhost'
banco = 'desafio_vendas'

engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}/{banco}')

df.to_sql('vendas_limpas', con=engine, if_exists='replace', index=False)

print("🎉 Sucesso! Seus dados já estão no MySQL.")
