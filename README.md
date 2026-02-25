## 𝜗ৎ Desafio Técnico em Tratamento e Análise de  Dados 𝜗ৎ

Neste exercício pegamos uma base de dados fictícia (vendas_raw.csv) com intenção de limpar e tratar os dados, transformando os datos em _dashboards_ e em seguida fazer análise para extração de _insights_.

---

### ⌕ Passo 1: Qualidade e Limpeza (_Python_) ⌕

Nesse passo foi feito o tratamento de dados usando o _Python_ por meio do _VSCode_.

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

---

 ### 🕮 Passo 2: Análise de Dados (SQL) 🕮

Após a limpieza dos dados no _Python_ foram feitas algumas _queries_ para responder perguntas propostas, que são vistas e respondidas juntamente com as linhas de comando usados. As _queries_ foram feitas pelo _MySQL Shell for VSCode_.

#### Qual o faturamento total por categoria?

> SELECT categoria, ROUND(SUM(valor_total), 2) AS faturamento 
FROM vendas_limpas GROUP BY categoria ORDER BY faturamento DESC;

<img width="337" height="153" alt="image" src="https://github.com/user-attachments/assets/bf4878ae-4007-4dd4-a230-7f58098fd679" />  
  
R.: Na categoria de **Acessórios** tivemos um faturamento toral de R$ 4685092,82.  
Na categoria de **Eletrodomésticos** tivemos R$ 3.698.535,20.  
A categoria de **Eletrônicos** teve um faturamento total de R$ 3.883.661,41.  
Com **Móveis** houve o faturamento de R$ 4.525.547,13.


#### Qual a região que mais vendeu em termos de quantidade de produtos?
  
> SELECT 
    regiao, 
    SUM(quantidade) AS total_produtos
FROM vendas_limpas
GROUP BY regiao
ORDER BY total_produtos DESC
LIMIT 1;

<img width="356" height="64" alt="image" src="https://github.com/user-attachments/assets/5b605897-8252-4ffa-96bc-76a1ee832b6c" />

R.: A região **Centro-oeste** foi a que mais teve vendas.

#### Quem são os 5 clientes que mais gastaram na loja?

> SELECT cliente, SUM(valor_total) AS total_gasto 
FROM vendas_limpas GROUP BY cliente ORDER BY total_gasto DESC LIMIT 5;

<img width="334" height="184" alt="image" src="https://github.com/user-attachments/assets/26b69d85-1b21-46b7-a38b-1b652d0cce9a" />
  
R.: Os clientes que mais gastaram na loja foram **Ágatha Leão**, **Antony da Cunha**, **Daniela Monteiro**, **Gustavo Azevedo** e **Cecilia Pires**.

#### Qual o ticket médio por venda?

> SELECT 
    ROUND(SUM(valor_total) / COUNT(id_venda), 2) AS ticket_medio 
FROM vendas_limpas;
  
<img width="157" height="64" alt="image" src="https://github.com/user-attachments/assets/e17e8204-1af6-497b-94b9-b70c92a4cb65" />
  
R.: O ticket médio por venda foi de **R$ 13.719,64**
  
**OBS.: O ticket médio é um indicador financeiro que mede o valor médio gasto por cliente por compra e é calculado dividindo o faturamento total pelo número de vendas.**

---
  
### ꩜ Passo 3: Visualização de Dados e Insights ꩜

Neste passo iniciamos a parte de vizualização de dados, e ela foi feita pelo Seaborn, que foi escolhida levando em conta a capacidade subjetiva de gerar visualizações estatísticas claras, sendo uma ferramenta muito eficiente para criar ótimos apoios visuais para gerar _insights_, principalmente considerando pessoas com menos conhecimento técnico.
Abaixo vemos os gráficos feitos a partes da base de dados de vendas limpo para responder visualmente as perguntas no passo 2.

#### Gráfico 1 - Faturamento total por Categoria
<img width="600" height="400" alt="grafico_faturamento_categoria" src="https://github.com/user-attachments/assets/2b015ba3-b2d8-4bb4-b936-40cb18066103" />

#### Gráfico 2 - Top 5 Clientes vs Média de Gasto por Pessoa
<img width="600" height="400" alt="grafico_top_clientes_vs_media" src="https://github.com/user-attachments/assets/8ca1a8d6-1110-49cf-89c1-3452e515f987" />

#### Gráfico 3 - Distribuição de Vendas por Região
<img width="600" height="400" alt="g3_vendas_regiao" src="https://github.com/user-attachments/assets/80df47c1-5d06-4a82-a59d-988cdf7161e4" />

  
#### Gráfico 4 - Distribuição de Faturamento por Região
<img width="600" height="400" alt="grafico_faturamento_regiao" src="https://github.com/user-attachments/assets/6c8495f9-fb49-40e7-9d3e-57df689a593e" />

    
### Insights a partir das informações retiradas dos dados:
⤷ Por categoria a maior quantidade de vendas está em acessórios (gráfico 1), tendo em vista que os acessórios costumam ser os menos custosos entre as opção é preciso observar a possibilidade de incentivo para venda de item mais estimados financeiramente.  
  
⤷ Observando a diferença dos gastos dos top 5 clientes para com a média geral de gastos (gráfico 2) vemos na diferença uma possibilidade de dependência de clientes específicos. Fica a proposta para criação de algum tipo de programa de fidelização de clientes.  
  
⤷ Apesar da região Centro-Oeste ter se mostrado como a região com mais vendas vemos que percentualmente ela tem a mesma quantidade que a região Norte (gráfico 3), mas quando olhamos para a distribuição de faturamente (gráfico 4) percebemos com mais clareza a diferença entre eles. Apesar disso a distribuição de vendas entre as regiões é relativamente harmônica.     
   
⤷ Vendo as inconsistências nos dados iniciais fica aparente que não é usado um sistema padronizado entre as lojas. Com problemas como a diferença de escrita entre as categorias e diferença de formatação de datas há a possibilidade de perda de dados e por isso a sugestão é que haja um sistema mais padronizado, com possibilidade de seleção de categorias, ao invés da escrita, e também seleção de data em formato preestabelecido. 
