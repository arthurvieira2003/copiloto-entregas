def processar_entregas(conexoes, entregas):
    # Construir a matriz de conexões
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
        # Se não houver conexão direta, encontrar o caminho mais curto
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

    def avaliar_entrega(entrega):
        tempo_inicio, destino, bonus = entrega
        tempo_viagem = calcular_tempo_viagem('A', destino)
        tempo_retorno = calcular_tempo_viagem(destino, 'A')
        tempo_total = tempo_viagem + tempo_retorno
        return {
            'entrega': entrega,
            'tempo_viagem': tempo_viagem,
            'tempo_retorno': tempo_retorno,
            'tempo_total': tempo_total,
            'lucro': bonus
        }

    def encontrar_melhor_entrega():
        melhor_entrega = None
        maior_lucro = 0
        for entrega in entregas:
            avaliacao = avaliar_entrega(entrega)
            if avaliacao['lucro'] > maior_lucro:
                maior_lucro = avaliacao['lucro']
                melhor_entrega = avaliacao
        return melhor_entrega

    melhor_entrega = encontrar_melhor_entrega()

    if melhor_entrega:
        return {
            "entregas_realizadas": [melhor_entrega['entrega']],
            "lucro_total": melhor_entrega['lucro']
        }
    else:
        return {
            "entregas_realizadas": [],
            "lucro_total": 0
        }