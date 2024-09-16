from itertools import combinations

def processar_entregas(conexoes, entregas):
    matriz_conexoes = {}
    for origem, destino, tempo in conexoes:
        if origem not in matriz_conexoes:
            matriz_conexoes[origem] = {}
        matriz_conexoes[origem][destino] = tempo
        if destino not in matriz_conexoes:
            matriz_conexoes[destino] = {}
        matriz_conexoes[destino][origem] = tempo

    def calcular_tempo_viagem(origem, destino):
        if destino in matriz_conexoes[origem]:
            return matriz_conexoes[origem][destino]
        caminho = encontrar_caminho_mais_curto(matriz_conexoes, origem, destino)
        if not caminho:
            return float('inf')
        tempo_total = 0
        for i in range(len(caminho) - 1):
            tempo_total += matriz_conexoes[caminho[i]][caminho[i+1]]
        return tempo_total

    def encontrar_caminho_mais_curto(grafo, inicio, fim):
        fila = [(inicio, [inicio])]
        visitados = set()
        while fila:
            (vertice, caminho) = fila.pop(0)
            if vertice not in visitados:
                if vertice == fim:
                    return caminho
                visitados.add(vertice)
                for proximo in grafo.get(vertice, {}):
                    if proximo not in visitados:
                        fila.append((proximo, caminho + [proximo]))
        return None

    def avaliar_entrega(entrega, tempo_atual):
        tempo_inicio, destino, bonus = entrega
        if tempo_inicio < tempo_atual:
            return None
        tempo_viagem = calcular_tempo_viagem('A', destino)
        tempo_retorno = calcular_tempo_viagem(destino, 'A')
        tempo_total = max(tempo_inicio - tempo_atual, 0) + tempo_viagem + tempo_retorno
        return {
            'entrega': entrega,
            'tempo_viagem': tempo_viagem,
            'tempo_retorno': tempo_retorno,
            'tempo_total': tempo_total,
            'lucro': bonus,
            'tempo_fim': tempo_atual + tempo_total
        }

    def encontrar_melhor_combinacao():
        melhor_combinacao = []
        maior_lucro = 0
        for i in range(1, len(entregas) + 1):
            for combo in combinations(entregas, i):
                tempo_atual = 0
                lucro_total = 0
                entregas_validas = []
                for entrega in combo:
                    avaliacao = avaliar_entrega(entrega, tempo_atual)
                    if avaliacao:
                        lucro_total += avaliacao['lucro']
                        tempo_atual = avaliacao['tempo_fim']
                        entregas_validas.append(avaliacao['entrega'])
                if lucro_total > maior_lucro:
                    maior_lucro = lucro_total
                    melhor_combinacao = entregas_validas
        return melhor_combinacao, maior_lucro

    melhor_combinacao, lucro_total = encontrar_melhor_combinacao()

    return {
        "entregas_realizadas": melhor_combinacao,
        "lucro_total": lucro_total
    }