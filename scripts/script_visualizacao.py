import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata

def limpar_texto(texto):
    if pd.isna(texto): return texto
    return unicodedata.normalize('NFKD', str(texto)).encode('ascii', 'ignore').decode('utf-8').upper()

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)

# Carregar os dados

df = pd.read_csv('data/vendas_cleaned.csv')

df['categoria'] = df['categoria'].apply(limpar_texto)
df['regiao'] = df['regiao'].apply(limpar_texto)

# Gráfico 1 - Faturamento Total por Categoria

plt.figure()
faturamento_cat = df.groupby('categoria')['valor_total'].sum().sort_values(ascending=False)
sns.barplot(x=faturamento_cat.values, y=faturamento_cat.index, hue=faturamento_cat.index, palette='viridis', legend=False)
plt.title('Faturamento Total por Categoria (Normalizado)', fontsize=15)
plt.xlabel('Faturamento (R$)')
plt.ylabel('Categoria')
plt.tight_layout()
plt.savefig('grafico_faturamento_categoria.png')

# Gráfico 2 - Top 5 Clientes

plt.figure()
top_clientes = df.groupby('cliente')['valor_total'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=top_clientes.index, y=top_clientes.values, hue=top_clientes.index, palette='magma', legend=False)
plt.title('Top 5 Clientes por Investimento Total', fontsize=15)
plt.xticks(rotation=45)
plt.ylabel('Total Gasto (R$)')
plt.tight_layout()
plt.savefig('grafico_top_clientes.png')

# Gráfico 3 - Top 5 Clientes vs. Gasto Médio Geral

plt.figure()
media_gasto = df['valor_total'].mean()
sns.barplot(x=top_clientes.index, y=top_clientes.values, hue=top_clientes.index, palette='magma', legend=False)
plt.axhline(y=media_gasto, color='orange', linestyle='--', label=f'Média Geral por Venda: R$ {media_gasto:.2f}')
plt.title('Top 5 Clientes vs. Média Geral de Gastos', fontsize=15)
plt.xticks(rotation=45)
plt.ylabel('Total Gasto (R$)')
plt.legend()
plt.tight_layout()
plt.savefig('grafico_top_clientes_vs_media.png')

# Gráfico 4 - Distribuição de Vendas por Região

plt.figure()
regiao_qtd = df.groupby('regiao')['quantidade'].sum().sort_values(ascending=False)
plt.pie(regiao_qtd, labels=regiao_qtd.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribuição de Quantidade de Itens por Região', fontsize=15)
plt.tight_layout()
plt.savefig('grafico_vendas_regiao.png')

# Gráfico 5 - Distribuição de Faturamento % por Região

plt.figure()
regiao_faturamento = df.groupby('regiao')['valor_total'].sum().sort_values(ascending=False)
plt.pie(regiao_faturamento, labels=regiao_faturamento.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Participação no Faturamento Total por Região', fontsize=15)
plt.tight_layout()
plt.savefig('grafico_faturamento_regiao.png')

# Gráfico 6 - Ticket Médio por Região

ticket_medio = (df.groupby('regiao')['valor_total'].sum() / df.groupby('regiao')['quantidade'].sum()).sort_values(ascending=False)
sns.barplot(x=ticket_medio.index, y=ticket_medio.values, hue=ticket_medio.index, palette='coolwarm', legend=False)
plt.title('Ticket Médio por Região (Faturamento/Qtd)', fontsize=15)   
plt.xlabel('Região')
plt.ylabel('Ticket Médio (R$)')
plt.tight_layout()
plt.savefig('grafico_ticket_medio_regiao.png')