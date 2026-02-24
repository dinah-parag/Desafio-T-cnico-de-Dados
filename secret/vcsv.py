import pandas as pd
import numpy as np  

from sqlalchemy import create_engine

usuario = 'root' 
senha = '280996'
host = 'localhost'
banco = 'desafio_vendas'

engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}/{banco}')

df.to_sql('vendas_limpas', con=engine, if_exists='replace', index=False)

print("🎉 Sucesso! Seus dados já estão no MySQL.")
