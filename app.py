import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Título e Descrição
st.title("Prática Técnica: Análise de Vendas")
st.markdown("""
Este dashboard apresenta resultados da análise de dados de vendas, 
passando pelo tratamento em Python e extração de insights.
""")

# Carregamento dos dados
@st.cache_data
def load_data():
    df = pd.read_csv("data/vendas_cleaned.csv") 
    df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')
    return df

try:
    df = load_data()

    # Filtros Interativos
    st.sidebar.header("Filtros")
    regiao_selecionada = st.sidebar.multiselect(
        "Selecione a Região:",
        options=df["regiao"].unique(),
        default=df["regiao"].unique()
    )

    # Filtrando o dataframe
    df_filtered = df[df["regiao"].isin(regiao_selecionada)]

    # MÉTRICAS PRINCIPAIS 
    col1, col2, col3 = st.columns(3)
    total_faturamento = df_filtered["valor_total"].sum()
    total_qtd = df_filtered["quantidade"].sum()
    ticket_medio = total_faturamento / total_qtd if total_qtd > 0 else 0

    col1.metric("Faturamento Total", f"R$ {total_faturamento:,.2f}")
    col2.metric("Qtd Total Vendida", f"{total_qtd:,.0f} unid.")
    col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

    st.divider()

    # GRÁFICOS INTERATIVOS
    c1, c2 = st.columns(2)

    with c1:
        # Faturamento por Categoria
        st.subheader("Faturamento por Categoria")
        faturamento_cat = df_filtered.groupby("categoria")["valor_total"].sum().reset_index().sort_values("valor_total", ascending=False)
        
        fig_cat = px.bar(
            faturamento_cat, 
            x="categoria", 
            y="valor_total",
            text_auto='.2s',
            labels={"valor_total": "Faturamento (R$)", "categoria": "Categoria"},
            color="valor_total",
            color_continuous_scale=px.colors.sequential.Mint 
        )
        fig_cat.update_layout(showlegend=False)
        st.plotly_chart(fig_cat, use_container_width=True)

    with c2:
        # Quantidade por Região
        st.subheader("Quantidade Vendida por Região")
        qtd_regiao = df_filtered.groupby("regiao")["quantidade"].sum().reset_index()
        
        fig_reg = px.pie(
            qtd_regiao, 
            values="quantidade", 
            names="regiao", 
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_reg, use_container_width=True)

    st.divider()

    # Top 5 Clientes vs Média de Gasto
    st.subheader("Top 5 Clientes: Faturamento e Média de Gasto")

    # Média de gasto por cliente    
    media_geral_venda = df_filtered["valor_total"].mean()

    analise_clientes = df_filtered.groupby("cliente").agg({
       "valor_total": ["sum", "mean"]
    }).reset_index()
    
    analise_clientes.columns = ["cliente", "faturamento_total", "media_gasto"]
    # Evita o NameError
    top_clientes = analise_clientes.sort_values("faturamento_total", ascending=False).head(5)

    fig_clientes = px.bar(
        top_clientes,
        x="cliente",
        y="faturamento_total",
        color="media_gasto",
        text_auto='.2s',
        labels={
            "faturamento_total": "Faturamento Total (R$)",
            "media_gasto": "Média de Gasto (R$)",
            "cliente": "Cliente"
        },
        color_continuous_scale=px.colors.sequential.Tealgrn,
        title="Faturamento por Cliente vs. Linha de Média Geral"
    )

    # Com linha da média geral
    fig_clientes.add_hline(
        y=media_geral_venda, 
        line_dash="dash", 
        line_color="orange",
        annotation_text=f"Média Geral: R$ {media_geral_venda:,.2f}", 
        annotation_position="top right"
    )
    
    fig_clientes.update_layout(coloraxis_colorbar=dict(title="Média (R$)"))
    st.plotly_chart(fig_clientes, use_container_width=True)
    
    # TABELA INTERATIVAs
    st.subheader("Exploração dos Dados Tratados")
    st.markdown("Abaixo você pode filtrar, ordenar e explorar a tabela completa.")
    st.dataframe(df_filtered, use_container_width=True)

except FileNotFoundError:
    st.error("Arquivo 'vendas_cleaned.csv' não encontrado na pasta 'data/'. Verifique se o nome no GitHub está correto.")