import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Carregar os dados

df = pd.read_csv('data/vendas_cleaned.csv')

# Gráfico 1 - Faturamento Total por Categoria

plt.figure()
faturamento_cat = df.groupby('categoria')['valor_total'].sum().sort_values(ascending=False)
sns.barplot(x=faturamento_cat.values, y=faturamento_cat.index, palette='viridis')
plt.title('Faturamento Total por Categoria', fontsize=15)
plt.xlabel('Faturamento (R$)')
plt.ylabel('Categoria')
plt.tight_layout()
plt.savefig('grafico_faturamento_categoria.png')

# Gráfico 2 - Top 5 Clientes

plt.figure()
top_clientes = df.groupby('cliente')['valor_total'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=top_clientes.index, y=top_clientes.values, palette='magma')
plt.title('Top 5 Clientes por Investimento Total', fontsize=15)
plt.xticks(rotation=45)
plt.ylabel('Total Gasto (R$)')
plt.tight_layout()
plt.savefig('grafico_top_clientes.png')

# Gráfico 3 - Distribuição de Vendas por Região

plt.figure()
regiao_qtd = df.groupby('regiao')['quantidade'].sum().sort_values(ascending=False)
plt.pie(regiao_qtd, labels=regiao_qtd.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribuição de Quantidade de Itens Vendidos por Região', fontsize=15)
plt.tight_layout()
plt.savefig('grafico_vendas_regiao.png')

