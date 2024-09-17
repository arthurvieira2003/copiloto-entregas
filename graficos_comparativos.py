import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from services.entrega_service import processar_entregas

def gerar_dados_simulacao(conexoes, entregas):
    resultado = processar_entregas(conexoes, entregas)
    entregas_realizadas = resultado['entregas_realizadas']
    lucro_total = resultado['lucro_total']
    
    tempos = [entrega[0] for entrega in entregas_realizadas]
    bonus = [entrega[2] for entrega in entregas_realizadas]
    destinos = [entrega[1] for entrega in entregas_realizadas]
    
    return pd.DataFrame({
        'Tempo de Início': tempos,
        'Bônus': bonus,
        'Destino': destinos
    })

def plotar_grafico_barras(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='bar', x='Destino', y='Bônus', ax=ax)
    plt.title('Bônus por Destino')
    plt.xlabel('Destino')
    plt.ylabel('Bônus')
    st.pyplot(fig)

def plotar_grafico_dispersao(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(df['Tempo de Início'], df['Bônus'], c=df.index, cmap='viridis')
    plt.colorbar(scatter)
    plt.title('Relação entre Tempo de Início e Bônus')
    plt.xlabel('Tempo de Início')
    plt.ylabel('Bônus')
    st.pyplot(fig)

def plotar_grafico_pizza(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    df.groupby('Destino')['Bônus'].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    plt.title('Distribuição de Bônus por Destino')
    st.pyplot(fig)

def main():
    st.title("Gráficos Comparativos de Entregas")

    conexoes = [
        ("A", "B", 5),
        ("B", "C", 3),
        ("A", "D", 2),
        ("C", "D", 8)
    ]
    
    entregas = [
        (0, "B", 10),
        (5, "C", 15),
        (10, "D", 20),
        (15, "B", 12),
        (20, "C", 18)
    ]

    df = gerar_dados_simulacao(conexoes, entregas)

    st.subheader("Dados das Entregas Realizadas")
    st.dataframe(df)

    st.subheader("Gráfico de Barras: Bônus por Destino")
    plotar_grafico_barras(df)

    st.subheader("Gráfico de Dispersão: Tempo de Início vs Bônus")
    plotar_grafico_dispersao(df)

    st.subheader("Gráfico de Pizza: Distribuição de Bônus por Destino")
    plotar_grafico_pizza(df)

if __name__ == "__main__":
    main()