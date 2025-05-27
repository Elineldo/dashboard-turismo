import streamlit as st
import pandas as pd
import plotly.express as px

# --- Dados Iniciais (predefinidos) ---
initial_data = [
    {"Source": "1. Macke et al.", "Impact": "Desenvolvimento do território", "Type": "Positivo", "Category": "Desenvolvimento Regional"},
    {"Source": "1. Macke et al.", "Impact": "Geração de capital social", "Type": "Positivo", "Category": "Social"},
    {"Source": "1. Macke et al.", "Impact": "Fortalecimento da gastronomia local", "Type": "Positivo", "Category": "Cultural/Econômico"},
    {"Source": "1. Macke et al.", "Impact": "Visibilidade à cultura local", "Type": "Positivo", "Category": "Cultural"},
    {"Source": "1. Macke et al.", "Impact": "Manutenção das tradições", "Type": "Positivo", "Category": "Cultural"},
    {"Source": "1. Macke et al.", "Impact": "Fortalece identidade", "Type": "Positivo", "Category": "Social/Cultural"},

    {"Source": "2. Zai & Sahr", "Impact": "Diversidade de atividades econômicas", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "2. Zai & Sahr", "Impact": "Especulação imobiliária, levando à saída de moradores e perda", "Type": "Negativo", "Category": "Social/Econômico"},
    {"Source": "2. Zai & Sahr", "Impact": "Melhoria da qualidade de vida pelo trabalho local", "Type": "Positivo", "Category": "Social"},
    {"Source": "2. Zai & Sahr", "Impact": "Fragilidade das APLs pela saída de moradores", "Type": "Negativo", "Category": "Social/Econômico"},
    {"Source": "2. Zai & Sahr", "Impact": "Conservação da biodiversidade", "Type": "Positivo", "Category": "Ambiental"},
    {"Source": "2. Zai & Sahr", "Impact": "Erosão de trilhas e áreas de cachoeiras", "Type": "Negativo", "Category": "Ambiental"},
    {"Source": "2. Zai & Sahr", "Impact": "Aumento de empregos para comunidade local", "Type": "Positivo", "Category": "Econômico/Social"},
    {"Source": "2. Zai & Sahr", "Impact": "Permanência das famílias no território", "Type": "Positivo", "Category": "Social"},
    {"Source": "2. Zai & Sahr", "Impact": "Coleta seletiva de lixo", "Type": "Positivo", "Category": "Ambiental"},
    {"Source": "2. Zai & Sahr", "Impact": "Invasão de propriedades particulares com atrativos", "Type": "Negativo", "Category": "Social"},
    {"Source": "2. Zai & Sahr", "Impact": "Aumento do consumo de bens e serviços locais", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "2. Zai & Sahr", "Impact": "Continuidade das atividades turísticas", "Type": "Positivo", "Category": "Geral"},
    {"Source": "2. Zai & Sahr", "Impact": "Degradação das estradas", "Type": "Negativo", "Category": "Infraestrutura"},
    {"Source": "2. Zai & Sahr", "Impact": "Aumento da geração de renda", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "2. Zai & Sahr", "Impact": "Fortalece identidade", "Type": "Positivo", "Category": "Social/Cultural"},
    {"Source": "2. Zai & Sahr", "Impact": "Valorização dos produtos rurais", "Type": "Positivo", "Category": "Econômico/Cultural"},

    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumento dos gastos dos turistas", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumenta visibilidade de comidas típicas", "Type": "Positivo", "Category": "Cultural/Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumento dos investimentos dos agentes locais, fomentando a cadeia de abastecimento", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Evasão de recursos na compra de suprimentos externos ao territòrio", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Fortalece identidade do território", "Type": "Positivo", "Category": "Social/Cultural"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumento dos empregos diretos locais", "Type": "Positivo", "Category": "Econômico/Social"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Concentração de renda nas traders pela venda de pacotes nacionais e internacionais", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Traders concentram visitas em locais específicos e deixam serviços locais de fora", "Type": "Negativo", "Category": "Econômico/Social"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Verticalização de produções em pequena escala", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Artesanatos têm pouca visibilidade quando são grandes traders", "Type": "Negativo", "Category": "Cultural/Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumento das vendas de produtos locais (processados ou in natura)", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Traders fazem pouca parceria com comunidades receptoras", "Type": "Negativo", "Category": "Social/Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumento dos serviços locais de hospedagem", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Aumento das distorções entre grandes e pequenos empreendimentos", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Remuneração mais baixa para serviços menos qualificados", "Type": "Negativo", "Category": "Econômico/Social"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Populações locais ficam à margem das atividades turísticas", "Type": "Negativo", "Category": "Social"},
    {"Source": "3. Silva et al. (Corumbá)", "Impact": "Inclusão sócio-produtiva", "Type": "Positivo", "Category": "Social/Econômico"},

    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Aumento do fluxo de turistas", "Type": "Positivo", "Category": "Geral"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Pouca sustentabilidade financeira dos circuitos turísticos", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Integração entre municípios dos territórios para trabalhar o turismo de forma regional", "Type": "Positivo", "Category": "Social/Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Aumento da burocracia", "Type": "Negativo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Maior permanência do turista na região", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Melhoria da relação com agentes estaduais", "Type": "Positivo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Falta de comprometimento dos agentes locais", "Type": "Negativo", "Category": "Social/Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Desenvolvimento econômico", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Sensibilização dos agentes locais sobre oportunidades turísticas", "Type": "Positivo", "Category": "Social/Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Aumento da arrecadação", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Maior autonomia pela descentralização da gestão do turismo", "Type": "Positivo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Aumento da visibilidade dos municípios já conhecidos como destino turístico", "Type": "Positivo", "Category": "Geral"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Ampliação dos municípios envolvidos com o turismo (interiorização das rotas)", "Type": "Positivo", "Category": "Geral"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Maior poder para negociar fontes de financiamento", "Type": "Positivo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Melhora da estrutura de governança do turismo", "Type": "Positivo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Modelos de implantação das rotas turísticas não considera características específica da região", "Type": "Negativo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Aumento da competitividade de grandes circuitos dificulta desenvolvimento de rotas menos conhecidas", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Dependência dos circuitos em relação às normas das SETUR, reduzindo autonomia na gestão dos circuitos", "Type": "Negativo", "Category": "Governança"},
    {"Source": "4. Silva et al. (Minas Gerais)", "Impact": "Poucos recursos da SETUR destinados à implementação dos circuitos", "Type": "Negativo", "Category": "Econômico/Governança"},

    {"Source": "5. Santos et al.", "Impact": "Sustentabilidade dos circuitos", "Type": "Positivo", "Category": "Sustentabilidade"},
    {"Source": "5. Santos et al.", "Impact": "Maior integração entre os agentes", "Type": "Positivo", "Category": "Social/Governança"},
    {"Source": "5. Santos et al.", "Impact": "Aumento da visitação", "Type": "Positivo", "Category": "Geral"},
    {"Source": "5. Santos et al.", "Impact": "Maior descentralização na gestão dos circuitos", "Type": "Positivo", "Category": "Governança"},
    {"Source": "5. Santos et al.", "Impact": "Aumento dos gastos dos turistas", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "5. Santos et al.", "Impact": "Maior cooperação intersetorial", "Type": "Positivo", "Category": "Social/Governança"},
    {"Source": "5. Santos et al.", "Impact": "Geração de empregos", "Type": "Positivo", "Category": "Econômico/Social"},
    {"Source": "5. Santos et al.", "Impact": "Inclusão social", "Type": "Positivo", "Category": "Social"},
    {"Source": "5. Santos et al.", "Impact": "Geração de renda", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "5. Santos et al.", "Impact": "Valorização do patrimônio cultural", "Type": "Positivo", "Category": "Cultural"},
    {"Source": "5. Santos et al.", "Impact": "Consolidação de destinos turísticos", "Type": "Positivo", "Category": "Geral"},
    {"Source": "5. Santos et al.", "Impact": "Melhora nas competências regionais em atividades turísticas", "Type": "Positivo", "Category": "Governança/Social"},
    {"Source": "5. Santos et al.", "Impact": "Atendimento ao anseio dos turistas", "Type": "Positivo", "Category": "Geral"},
    {"Source": "5. Santos et al.", "Impact": "Aumenta competitividade frente a outros circuitos turísticos", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "5. Santos et al.", "Impact": "Falta de infraestrutura pode ser marketing negativo", "Type": "Negativo", "Category": "Infraestrutura"},
    {"Source": "5. Santos et al.", "Impact": "Aumento das vagas de hospedagem", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "5. Santos et al.", "Impact": "Maiores comodidades de locomoção, gerando empregos de receptivos", "Type": "Positivo", "Category": "Econômico/Infraestrutura"},

    {"Source": "6. Bondarenko", "Impact": "Acréscimo de receita", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "6. Bondarenko", "Impact": "Custos com infraestrutura", "Type": "Negativo", "Category": "Econômico/Infraestrutura"},
    {"Source": "6. Bondarenko", "Impact": "Intercâmbio sociocultural entre o turista e habitantes locais", "Type": "Positivo", "Category": "Social/Cultural"},
    {"Source": "6. Bondarenko", "Impact": "Conflitos por diferenças culturais", "Type": "Negativo", "Category": "Social/Cultural"},
    {"Source": "6. Bondarenko", "Impact": "Geração de postos de trabalho", "Type": "Positivo", "Category": "Econômico/Social"},
    {"Source": "6. Bondarenko", "Impact": "Inflação dos preços locais", "Type": "Negativo", "Category": "Econômico"},
    {"Source": "6. Bondarenko", "Impact": "Saturação dos habitantes locais pela presença constante de turistas", "Type": "Negativo", "Category": "Social"},
    {"Source": "6. Bondarenko", "Impact": "Geração de oportunidades de negócio", "Type": "Positivo", "Category": "Econômico"},
    {"Source": "6. Bondarenko", "Impact": "Capacidade ociosa em turismo sazonal", "Type": "Negativo", "Category": "Econômico"}
]

# Inicializa o DataFrame no session_state se ainda não existir
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(initial_data)

# --- Funções Auxiliares ---
def add_data_to_df(new_data_dict):
    """Adiciona uma nova linha de dados ao DataFrame no session_state."""
    new_df_row = pd.DataFrame([new_data_dict])
    st.session_state.df = pd.concat([st.session_state.df, new_df_row], ignore_index=True)

def reset_data():
    """Reseta o DataFrame para os dados iniciais."""
    st.session_state.df = pd.DataFrame(initial_data)
    st.success("Dados resetados para o conjunto inicial.")

# --- Título e Introdução do Dashboard ---
st.title("Dashboard de Análise de Impactos do Turismo")

st.markdown("""
Este dashboard apresenta uma análise dos impactos do turismo, baseada em diversas fontes de pesquisa.
Você pode explorar os dados usando os filtros e gráficos, além de **adicionar seus próprios dados**
através de upload de arquivo ou formulário manual.
""")

# --- Seção para Adicionar Dados ---
st.sidebar.header("Adicionar Novos Dados")

# Botão para resetar os dados
st.sidebar.button("Resetar Dados para o Padrão", on_click=reset_data)

# Upload de Arquivo
st.sidebar.subheader("Importar por Arquivo (.csv, .xlsx)")
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            new_data_df = pd.read_csv(uploaded_file)
        else: # .xlsx
            new_data_df = pd.read_excel(uploaded_file)

        # Verificar se as colunas essenciais existem
        required_columns = ["Source", "Impact", "Type", "Category"]
        if not all(col in new_data_df.columns for col in required_columns):
            st.sidebar.error(f"O arquivo deve conter as colunas: {', '.join(required_columns)}")
        else:
            st.session_state.df = pd.concat([st.session_state.df, new_data_df[required_columns]], ignore_index=True)
            st.sidebar.success("Dados do arquivo importados com sucesso!")
    except Exception as e:
        st.sidebar.error(f"Erro ao ler o arquivo: {e}")

# Formulário de Entrada Manual
st.sidebar.subheader("Entrada Manual de Dados")
with st.sidebar.form("manual_data_entry"):
    new_source = st.text_input("Fonte:", "Novo Estudo")
    new_impact = st.text_input("Impacto:", "Novo impacto positivo")
    new_type = st.selectbox("Tipo:", ["Positivo", "Negativo"])
    new_category = st.selectbox("Categoria:", sorted(list(st.session_state.df["Category"].unique()) + ["Outros", "Governança", "Sustentabilidade", "Ambiental", "Infraestrutura"]))

    submitted = st.form_submit_button("Adicionar Impacto")
    if submitted:
        if new_impact and new_source and new_type and new_category:
            add_data_to_df({
                "Source": new_source,
                "Impact": new_impact,
                "Type": new_type,
                "Category": new_category
            })
            st.sidebar.success("Impacto adicionado com sucesso!")
        else:
            st.sidebar.error("Por favor, preencha todos os campos do formulário.")


# --- Filtros (Agora usam o DataFrame do session_state) ---
st.header("Filtros")

# Filtro por Fonte
all_sources = st.session_state.df["Source"].unique().tolist()
selected_sources = st.multiselect(
    "Selecione a(s) Fonte(s):",
    options=all_sources,
    default=all_sources
)

# Filtro por Categoria
all_categories = sorted(list(st.session_state.df["Category"].unique()))
selected_categories = st.multiselect(
    "Selecione a(s) Categoria(s):",
    options=all_categories,
    default=all_categories
)

# Filtro por Tipo de Impacto
selected_types = st.multiselect(
    "Selecione o(s) Tipo(s) de Impacto:",
    options=st.session_state.df["Type"].unique().tolist(),
    default=st.session_state.df["Type"].unique().tolist()
)

# Aplica os filtros ao DataFrame atual do session_state
filtered_df = st.session_state.df[
    st.session_state.df["Source"].isin(selected_sources) &
    st.session_state.df["Category"].isin(selected_categories) &
    st.session_state.df["Type"].isin(selected_types)
]

# --- Exibição dos Dados Filtrados ---
st.header("Dados Filtrados")
if filtered_df.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados. Tente ajustar os filtros ou adicionar mais dados.")
else:
    st.dataframe(filtered_df, use_container_width=True)

# --- Análise e Visualizações ---
st.header("Visualizações")

# Gráfico de pizza: Proporção de Impactos Positivos vs. Negativos
st.subheader("Proporção de Impactos Positivos e Negativos")
if not filtered_df.empty:
    impact_type_counts = filtered_df["Type"].value_counts().reset_index()
    impact_type_counts.columns = ["Tipo de Impacto", "Contagem"]
    fig_pie = px.pie(
        impact_type_counts,
        values="Contagem",
        names="Tipo de Impacto",
        title="Proporção Geral de Impactos",
        color="Tipo de Impacto",
        color_discrete_map={"Positivo": "green", "Negativo": "red"},
        hole=0.3 # Adiciona um buraco para um visual de 'donut'
    )
    st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.info("Filtre os dados para ver o gráfico de proporção de impactos.")


# Gráfico de barras: Contagem de Impactos por Tipo
st.subheader("Contagem de Impactos por Tipo")
if not filtered_df.empty:
    impact_type_counts = filtered_df["Type"].value_counts().reset_index()
    impact_type_counts.columns = ["Tipo de Impacto", "Contagem"]
    fig_type = px.bar(
        impact_type_counts,
        x="Tipo de Impacto",
        y="Contagem",
        color="Tipo de Impacto",
        title="Distribuição de Impactos Positivos e Negativos",
        labels={"Tipo de Impacto": "Tipo", "Contagem": "Número de Impactos"},
        color_discrete_map={"Positivo": "green", "Negativo": "red"}
    )
    st.plotly_chart(fig_type, use_container_width=True)
else:
    st.info("Filtre os dados para ver o gráfico de contagem de impactos.")

# Gráfico de barras empilhadas: Contagem de Impactos por Categoria e Tipo
st.subheader("Impactos Positivos e Negativos por Categoria")
if not filtered_df.empty:
    category_type_counts = filtered_df.groupby(["Category", "Type"]).size().reset_index(name="Contagem")
    fig_stacked_bar = px.bar(
        category_type_counts,
        x="Category",
        y="Contagem",
        color="Type",
        title="Distribuição de Impactos Positivos e Negativos por Categoria",
        labels={"Category": "Categoria", "Contagem": "Número de Impactos", "Type": "Tipo"},
        color_discrete_map={"Positivo": "green", "Negativo": "red"},
        barmode='stack' # Define o modo de barras como empilhado
    )
    st.plotly_chart(fig_stacked_bar, use_container_width=True)
else:
    st.info("Filtre os dados para ver o gráfico de impactos por categoria e tipo.")


# Gráfico de barras: Contagem de Impactos por Fonte e Tipo
st.subheader("Contagem de Impactos por Fonte e Tipo")
if not filtered_df.empty:
    source_type_counts = filtered_df.groupby(["Source", "Type"]).size().reset_index(name="Contagem")
    fig_source_type = px.bar(
        source_type_counts,
        x="Source",
        y="Contagem",
        color="Type",
        title="Impactos por Fonte e Tipo",
        labels={"Source": "Fonte", "Contagem": "Número de Impactos", "Type": "Tipo"},
        color_discrete_map={"Positivo": "green", "Negativo": "red"}
    )
    st.plotly_chart(fig_source_type, use_container_width=True)
else:
    st.info("Filtre os dados para ver o gráfico de impactos por fonte.")

# --- Resumo da Análise ---
st.header("Resumo da Análise")
if not filtered_df.empty:
    total_impacts = len(filtered_df)
    positive_impacts = filtered_df[filtered_df["Type"] == "Positivo"].shape[0]
    negative_impacts = filtered_df[filtered_df["Type"] == "Negativo"].shape[0]

    st.markdown(f"""
    Com base nos filtros aplicados, foram identificados **{total_impacts}** impactos no total.
    * **Impactos Positivos:** {positive_impacts} ({positive_impacts / total_impacts:.1%})
    * **Impactos Negativos:** {negative_impacts} ({negative_impacts / total_impacts:.1%})
    """)

    st.markdown("---")
    st.markdown("""
    **Análise Detalhada dos Impactos do Turismo:**

    A análise dos dados revela uma complexa interação de efeitos positivos e negativos gerados pelo turismo, abrangendo diversas dimensões como a econômica, social, cultural, ambiental, de governança e infraestrutura.

    **1. Equilíbrio entre Positivos e Negativos:**
    O gráfico de pizza "Proporção Geral de Impactos" oferece uma visão imediata do balanço entre os impactos. Embora o turismo seja frequentemente promovido por seus benefícios, a presença de um número significativo de impactos negativos sublinha a necessidade de planejamento e gestão cuidadosos para mitigar riscos e maximizar os retornos positivos.

    **2. Impactos por Categoria:**
    O gráfico de barras empilhadas "Impactos Positivos e Negativos por Categoria" é crucial para entender onde o turismo gera mais valor e onde enfrenta maiores desafios:
    * **Econômico:** Esta é a categoria com maior número de impactos, tanto positivos (aumento de gastos, geração de renda, empregos, investimentos) quanto negativos (evasão de recursos, concentração de renda, inflação, verticalização de produções). Isso sugere que, embora o turismo seja um motor econômico, a distribuição de seus benefícios e a gestão de custos são pontos críticos.
    * **Social:** Com impactos como geração de capital social, melhoria da qualidade de vida e inclusão sócio-produtiva, o turismo tem um potencial significativo para o desenvolvimento comunitário. No entanto, desafios como especulação imobiliária, fragilidade de APLs (Arranjos Produtivos Locais) e saturação dos habitantes locais são preocupações que exigem atenção.
    * **Cultural:** O turismo fortalece a identidade, valoriza o patrimônio e a gastronomia local, mas também pode gerar conflitos culturais e pouca visibilidade para artesanatos locais quando há predominância de grandes operadores.
    * **Ambiental:** A conservação da biodiversidade é um impacto positivo, mas a degradação de trilhas e áreas naturais aponta para a necessidade de práticas de turismo sustentável.
    * **Governança:** A integração entre municípios e a descentralização da gestão são impactos positivos importantes, mas a burocracia, a falta de comprometimento dos agentes locais e a dependência de normas estaduais podem limitar o potencial de desenvolvimento.
    * **Infraestrutura:** Embora o turismo possa impulsionar melhorias na infraestrutura (hospedagem, locomoção), também pode levar à degradação de estradas e custos elevados, além de ser um fator de marketing negativo se for deficiente.

    **3. Impactos por Fonte (Estudos):**
    O gráfico "Impactos por Fonte e Tipo" permite comparar as percepções e os focos de cada estudo:
    * Estudos como o de **Macke et al.** e **Zai & Sahr** tendem a focar mais nos impactos regionais, sociais e ambientais, destacando tanto o desenvolvimento do território quanto os desafios de especulação e degradação.
    * **Silva et al. (Corumbá)** aprofunda-se nos aspectos econômicos e sociais, revelando tensões entre grandes e pequenos empreendimentos e a inclusão das comunidades locais.
    * **Silva et al. (Minas Gerais)** e **Santos et al.** abordam a regionalização do turismo, governança e sustentabilidade dos circuitos, com ênfase na integração e nos desafios de infraestrutura e burocracia.
    * **Bondarenko** oferece uma perspectiva mais econômica, com foco em receita, custos e oportunidades de negócio, mas também alerta para a inflação e a saturação local.

    **Conclusão:**
    A análise demonstra que o turismo é uma força transformadora com a capacidade de impulsionar o desenvolvimento econômico e social, valorizar a cultura e gerar empregos. No entanto, para que esses benefícios sejam sustentáveis e equitativos, é fundamental abordar proativamente os desafios como a especulação imobiliária, a degradação ambiental, a concentração de renda e as fragilidades na governança. Um planejamento estratégico que priorize a inclusão das comunidades locais, a sustentabilidade e a integração entre os diversos agentes é essencial para otimizar os impactos positivos e minimizar os negativos do turismo.
    """)
else:
    st.info("Nenhum dado para resumir. Por favor, ajuste os filtros ou adicione mais dados.")