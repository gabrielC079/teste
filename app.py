import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Completo do Banco de Dados")

# Lendo o CSV
url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/main/dataset_tratado.csv"
df = pd.read_csv(url)

st.subheader("Prévia dos dados")
st.dataframe(df)

# -----------------------------
# 1. HISTOGRAMAS
# -----------------------------
st.header("📌 Histogramas")

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    fig = px.histogram(df, x=col, nbins=20, title=f"Distribuição de {col}")
    st.plotly_chart(fig)

    st.markdown(f"""
    **Observação:**  
    A distribuição da variável **{col}** mostra como os valores se espalham no conjunto de dados.  
    Isso ajuda a identificar concentrações, extremos e padrões gerais.
    """)

# -----------------------------
# 2. DISPERSÕES
# -----------------------------
st.header("📌 Gráficos de Dispersão")

if "daily_calories_consumed" in df.columns and "weight_change_(lbs)" in df.columns:
    fig = px.scatter(df, x="daily_calories_consumed", y="weight_change_(lbs)",
                     color="gender", title="Calorias Consumidas vs Mudança de Peso")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    Existe uma relação clara entre o consumo diário de calorias e a mudança de peso.  
    Indivíduos que consomem mais calorias tendem a apresentar maior ganho de peso.
    """)

if "daily_caloric_surplus/deficit" in df.columns and "weight_change_(lbs)" in df.columns:
    fig = px.scatter(df, x="daily_caloric_surplus/deficit", y="weight_change_(lbs)",
                     color="physical_activity_level",
                     title="Superávit/Déficit Calórico vs Mudança de Peso")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    Déficits calóricos estão associados à perda de peso, enquanto superávits levam ao ganho.  
    O nível de atividade física influencia essa relação.
    """)

# -----------------------------
# 3. BOXPLOTS
# -----------------------------
st.header("📌 Boxplots")

if "physical_activity_level" in df.columns:
    fig = px.box(df, x="physical_activity_level", y="weight_change_(lbs)",
                 title="Mudança de Peso por Nível de Atividade Física")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    Pessoas mais ativas tendem a apresentar menor ganho de peso.  
    A atividade física funciona como fator protetor.
    """)

if "sleep_quality" in df.columns:
    fig = px.box(df, x="sleep_quality", y="weight_change_(lbs)",
                 title="Mudança de Peso por Qualidade do Sono")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    Melhor qualidade de sono está associada a menor oscilação de peso.  
    O sono influencia o equilíbrio metabólico.
    """)

# -----------------------------
# 4. CORRELAÇÃO
# -----------------------------
st.header("📌 Mapa de Correlação")

corr = df[num_cols].corr()
fig = px.imshow(corr, text_auto=True, color_continuous_scale="Blues",
                title="Correlação entre Variáveis Numéricas")
st.plotly_chart(fig)

st.markdown("""
**Observação:**  
O mapa de correlação revela relações fortes entre peso inicial, peso final e mudança de peso.  
Também mostra coerência entre calorias consumidas e superávit/déficit.
""")

# -----------------------------
# 5. BARRAS
# -----------------------------
st.header("📌 Gráficos de Barras")

if "gender" in df.columns:
    fig = px.bar(df.groupby("gender")["weight_change_(lbs)"].mean().reset_index(),
                 x="gender", y="weight_change_(lbs)",
                 title="Mudança de Peso por Gênero")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    A mudança média de peso varia entre os gêneros, indicando diferenças fisiológicas ou comportamentais.
    """)

if "stress_level" in df.columns:
    fig = px.bar(df.groupby("stress_level")["weight_change_(lbs)"].mean().reset_index(),
                 x="stress_level", y="weight_change_(lbs)",
                 title="Mudança de Peso por Nível de Estresse")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    Níveis mais altos de estresse estão associados a maior variação de peso.  
    O estresse afeta comportamento alimentar e metabolismo.
    """)

# -----------------------------
# 6. LINHA
# -----------------------------
st.header("📌 Gráfico de Linha")

if "duration_(weeks)" in df.columns:
    fig = px.line(df.sort_values("duration_(weeks)"),
                  x="duration_(weeks)", y="weight_change_(lbs)",
                  title="Mudança de Peso ao Longo das Semanas")
    st.plotly_chart(fig)

    st.markdown("""
    **Observação:**  
    A mudança de peso ao longo das semanas mostra uma tendência gradual.  
    Isso reforça que transformações corporais acontecem de forma progressiva.
    """)

