def processar_entregas(conexoes, entregas):
    # Construir a matriz de conexões
    matriz_conexoes = {}
    for origem, destino, tempo in conexoes:
        if origem not in matriz_conexoes:
            matriz_conexoes[origem] = {}
        matriz_conexoes[origem][destino] = tempo
        if destino not in matriz_conexoes:
            matriz_conexoes[destino] = {}
        if origem not in matriz_conexoes[destino]:
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

    def explorar_entregas():
        melhor_resultado = {"entregas_realizadas": [], "lucro_total": 0}

        # Opção 1: Realizar todas as entregas possíveis sem espera
        tempo_atual = 0
        lucro_total = 0
        entregas_realizadas = []
        for tempo_inicio, destino, bonus in sorted(entregas):
            tempo_viagem = calcular_tempo_viagem('A', destino)
            tempo_chegada = max(tempo_atual + tempo_viagem, tempo_inicio)
            if tempo_chegada <= tempo_inicio or (tempo_atual <= tempo_inicio):
                entregas_realizadas.append([tempo_inicio, destino, bonus])
                lucro_total += bonus
                tempo_atual = tempo_chegada + calcular_tempo_viagem(destino, 'A')

        if lucro_total > melhor_resultado["lucro_total"]:
            melhor_resultado = {"entregas_realizadas": entregas_realizadas, "lucro_total": lucro_total}

        # Opção 2: Esperar e realizar apenas a entrega mais lucrativa
        for tempo_inicio, destino, bonus in entregas:
            tempo_viagem = calcular_tempo_viagem('A', destino)
            tempo_chegada = max(tempo_inicio, tempo_viagem)
            tempo_retorno = tempo_chegada + calcular_tempo_viagem(destino, 'A')
            
            if bonus > melhor_resultado["lucro_total"]:
                melhor_resultado = {
                    "entregas_realizadas": [[tempo_inicio, destino, bonus]],
                    "lucro_total": bonus
                }

        return melhor_resultado

    return explorar_entregas()