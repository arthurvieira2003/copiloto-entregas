import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from services.entrega_service import processar_entregas

def criar_grafo(conexoes):
    G = nx.Graph()
    for origem, destino, tempo in conexoes:
        G.add_edge(origem, destino, weight=tempo)
    return G

def plotar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Mapa de Conexões")
    st.pyplot(plt)

def main():
    st.title("Simulação Visual de Seleção de Entregas")

    st.header("Configuração")
    num_conexoes = st.number_input("Número de conexões", min_value=1, value=3)
    num_entregas = st.number_input("Número de entregas", min_value=1, value=3)

    conexoes = []
    for i in range(num_conexoes):
        col1, col2, col3 = st.columns(3)
        origem = col1.text_input(f"Origem {i+1}", value="A")
        destino = col2.text_input(f"Destino {i+1}", value="B")
        tempo = col3.number_input(f"Tempo {i+1}", min_value=1, value=5)
        conexoes.append((origem, destino, tempo))

    entregas = []
    for i in range(num_entregas):
        col1, col2, col3 = st.columns(3)
        tempo_inicio = col1.number_input(f"Tempo de início {i+1}", min_value=0, value=0)
        destino = col2.text_input(f"Destino da entrega {i+1}", value="B")
        bonus = col3.number_input(f"Bônus {i+1}", min_value=1, value=10)
        entregas.append((tempo_inicio, destino, bonus))

    if st.button("Processar Entregas"):
        G = criar_grafo(conexoes)
        plotar_grafo(G)

        resultado = processar_entregas(conexoes, entregas)

        st.header("Resultados")
        st.write(f"Lucro Total: {resultado['lucro_total']}")
        st.write("Entregas Realizadas:")
        for entrega in resultado['entregas_realizadas']:
            st.write(f"- Tempo: {entrega[0]}, Destino: {entrega[1]}, Bônus: {entrega[2]}")

if __name__ == "__main__":
    main()