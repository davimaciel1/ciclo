
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("🌎 Análise de Ciclos Fundamentalistas")
st.markdown("Visualize a evolução dos trimestres em quadrantes com base na Receita e EBITDA (YoY).")

# Dados de exemplo para WEGE3 (substituir depois com dados dinâmicos ou API)
data = {
    'Trimestre': ['1T21', '2T21', '3T21', '4T21', '1T22', '2T22', '3T22', '4T22', '1T23', '2T23'],
    'Receita YoY (%)': [25, 28, 24, 22, 20, 18, 15, 10, 12, 14],
    'EBITDA YoY (%)': [30, 35, 32, 28, 25, 20, 10, 5, 8, 10]
}

df = pd.DataFrame(data)
df['Receita YoY'] = df['Receita YoY (%)'] / 100
df['EBITDA YoY'] = df['EBITDA YoY (%)'] / 100

# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Linhas dos quadrantes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Fundo colorido dos quadrantes
ax.set_facecolor('white')
ax.fill_between([-0.5, 0], 0, 0.5, facecolor='lightblue', alpha=0.3)   # Recuperação
ax.fill_between([0, 0.5], 0, 0.5, facecolor='lightgreen', alpha=0.3)  # Expansão
ax.fill_between([0, 0.5], -0.5, 0, facecolor='khaki', alpha=0.3)      # Retração
ax.fill_between([-0.5, 0], -0.5, 0, facecolor='lightcoral', alpha=0.3) # Desaceleração

# Plotagem do ciclo
ax.plot(df['Receita YoY'], df['EBITDA YoY'], marker='o', color='blue', linewidth=2)

# Rótulos
for i, row in df.iterrows():
    ax.text(row['Receita YoY'], row['EBITDA YoY'], row['Trimestre'], fontsize=9, ha='left')

ax.set_xlabel('Receita YoY (%)')
ax.set_ylabel('EBITDA YoY (%)')
ax.set_title('Ciclo Fundamentalista da Empresa (WEGE3)')
ax.grid(True)
plt.xlim(-0.5, 0.5)
plt.ylim(-0.5, 0.5)

st.pyplot(fig)
