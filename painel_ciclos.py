import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Ciclo Fundamentalista da Empresa (WEGE3)")
st.markdown("Visualize os quadrantes econômicos com base em Receita e EBITDA YoY, junto com o preço do ativo.")

# Leitura do CSV com dados reais
df = pd.read_csv("dados_fundamentalistas_wege3.csv")
df['Receita YoY (%)'] = df['Receita YoY'] * 100
df['EBITDA YoY (%)'] = df['EBITDA YoY'] * 100

# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Fundo dos quadrantes
ax.fill_between([-0.5, 0], 0, 0.5, facecolor='lightblue', alpha=0.3)   # Recuperação
ax.fill_between([0, 0.5], 0, 0.5, facecolor='lightgreen', alpha=0.3)  # Expansão
ax.fill_between([0, 0.5], -0.5, 0, facecolor='khaki', alpha=0.3)      # Retração
ax.fill_between([-0.5, 0], -0.5, 0, facecolor='lightcoral', alpha=0.3) # Desaceleração

# Rótulos dos quadrantes
ax.text(-0.45, 0.42, "Recuperação", fontsize=10, weight='bold')
ax.text(0.25, 0.42, "Expansão", fontsize=10, weight='bold')
ax.text(-0.45, -0.42, "Desaceleração", fontsize=10, weight='bold')
ax.text(0.25, -0.42, "Retração", fontsize=10, weight='bold')

# Plotagem
ax.plot(df['Receita YoY'], df['EBITDA YoY'], marker='o', color='blue', linewidth=2)

# Trimestres + preço
for i, row in df.iterrows():
    label = f"{row['Trimestre']}\nR$ {row['Preço Ajustado']:.2f}"
    ax.text(row['Receita YoY'], row['EBITDA YoY'], label, fontsize=8, ha='left')

ax.set_xlabel('Receita YoY (%)')
ax.set_ylabel('EBITDA YoY (%)')
ax.grid(True)
plt.xlim(-0.5, 0.5)
plt.ylim(-0.5, 0.5)

st.pyplot(fig)

# Correlação
st.subheader("🔍 Correlação entre fundamentos e preço")
with open("correlacao_wege3.txt", "r") as file:
    correl_info = file.read()
st.code(correl_info)

# Alerta inteligente
st.subheader("🚨 Alerta Inteligente")
ultimo = df.iloc[-1]
anterior = df.iloc[-2]
if (ultimo['EBITDA YoY'] > anterior['EBITDA YoY']) and (ultimo['Preço Ajustado'] <= anterior['Preço Ajustado']):
    st.warning("EBITDA YoY está acelerando, mas o preço ainda não subiu. Isso pode indicar uma oportunidade!")
else:
    st.success("Sem anomalias detectadas entre EBITDA e preço no último trimestre.")
