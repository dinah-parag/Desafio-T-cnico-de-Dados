import pandas as pd
from sqlalchemy import create_engine
import os


caminho = os.path.join('data', 'vendas_raw.csv')
df = pd.read_csv(caminho)

usuario = 'root' 
senha = '**' 
host = 'localhost'
banco = 'desafio_vendas'

engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}/{banco}')

# criação da tabela 'vendas_limpas' no 'desafio_vendas'
df.to_sql('vendas_limpas', con=engine, if_exists='replace', index=False)

print("Processo concluído: Arquivo lido da pasta 'data' e salvo no MySQL!")