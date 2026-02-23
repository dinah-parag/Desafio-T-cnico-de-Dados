## 𝜗ৎ Desafio Técnico em Tratamento e Análise de  Dados 𝜗ৎ

Neste exercício pegamos uma base de dados fictícia (vendas_raw.csv) com intenção de limpar e tratar os dados, transformando os datos em _dashboards_ e em seguida fazer análise para extração de _insights_.

### Passo 1: Qualidade e Limpeza (Python)
➴ Tratamento de Nulos;  
➴ Anonimização de dados sensíveis;  
➴ Padronização de Datas;  
➴ Normalização de Categorias;  

#### Dicionário de Dados tratados: 

| COLUNA | TIPO | DESCRIÇÃO |
| :--- | :---: | ---: |
| id_venda | Int | Identificador único da venda |
| data_venda | String | Data da venda formatada (YYYY-MM-DD) ou 'Data não informada' |
| cliente | String | Nome do cliente ou 'Não Identificado' |
| email_cliente | String | E-mail mascarado e de acordo com LGPD |
| produto | String | Nome do produto vendido|
| categoria | String | Categoria padronizada (Ex: Eletrônicos) |
| quantidade | Float/Int | Quantidade de itens vendidos |
| preco_unitario | Float | Preço de cada unidade (recuperado se nulo) |
| valor_total | Float | Preço total da transação |
| regiao | String | Região geográfica da venda |

<!-- ### Passo 2: Análise de Dados (SQL)
Com os dados limpos, responda às seguintes perguntas usando consultas SQL: obs: envie os dados limpos para um banco de dados de sua preferencia

Qual o faturamento total por categoria?
Qual a região que mais vendeu em termos de quantidade de produtos?
Quem são os 5 clientes que mais gastaram na loja?
Qual o ticket médio por venda?

### Passo 3: Visualização de Dados e Insights
Criação de Gráficos: Desenvolva pelo menos 3 gráficos (utilizando bibliotecas Python como Matplotlib, Seaborn, Plotly ou até mesmo ferramentas de BI como Power BI/Looker Studio) para ilustrar os resultados das perguntas da etapa de SQL ou demonstrar outros padrões interessantes.
Comunicação: Crie um pequeno relatório (pode ser no README) detalhando pelo menos 3 insights relevantes que você detectou com base nas suas análises e visualizações.
