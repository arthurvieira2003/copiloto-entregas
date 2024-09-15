def processar_entregas(conexoes, entregas):
    # Construir a matriz de conexões
    matriz_conexoes = {}
    for origem, destino, tempo in conexoes:
        if origem not in matriz_conexoes:
            matriz_conexoes[origem] = {}
        matriz_conexoes[origem][destino] = tempo
        # Adicionar a conexão reversa se não existir
        if destino not in matriz_conexoes:
            matriz_conexoes[destino] = {}
        if origem not in matriz_conexoes[destino]:
            matriz_conexoes[destino][origem] = tempo

    # Função recursiva para explorar todas as combinações possíveis de entregas
    def explorar_entregas(origem_atual, tempo_atual, entregas_pendentes, entregas_realizadas, lucro_atual):
        nonlocal max_lucro, melhor_sequencia

        # Atualizar lucro máximo se a sequência atual for melhor
        if lucro_atual > max_lucro:
            max_lucro = lucro_atual
            melhor_sequencia = list(entregas_realizadas)

        # Tentar todas as entregas restantes
        for i, (tempo_inicio, destino, bonus) in enumerate(entregas_pendentes):
            # Verificar se a entrega é possível a partir do ponto atual
            if origem_atual in matriz_conexoes and destino in matriz_conexoes[origem_atual]:
                tempo_viagem = matriz_conexoes[origem_atual][destino]
                
                # Calcular o tempo de chegada para fazer a entrega
                tempo_chegada = max(tempo_atual + tempo_viagem, tempo_inicio)

                # Verificar se conseguimos fazer a entrega a tempo
                if tempo_chegada <= tempo_inicio or (origem_atual == 'A' and tempo_atual <= tempo_inicio):
                    # Calcular o tempo total incluindo o retorno para 'A'
                    tempo_retorno = tempo_chegada
                    if destino in matriz_conexoes and 'A' in matriz_conexoes[destino]:
                        tempo_retorno += matriz_conexoes[destino]['A']
                    else:
                        # Se não houver conexão direta, usamos o caminho mais curto
                        caminho_retorno = encontrar_caminho_mais_curto(matriz_conexoes, destino, 'A')
                        if caminho_retorno:
                            for j in range(len(caminho_retorno) - 1):
                                tempo_retorno += matriz_conexoes[caminho_retorno[j]][caminho_retorno[j+1]]
                        else:
                            # Se não encontrarmos um caminho, pulamos esta entrega
                            continue
                    
                    # Filtrar a lista de entregas removendo a entrega atual e as que não podem mais ser feitas
                    nova_lista_entregas = [
                        (t, d, b) for j, (t, d, b) in enumerate(entregas_pendentes)
                        if j != i and t > tempo_chegada
                    ]

                    # Explorar com esta entrega realizada
                    explorar_entregas(
                        'A',  # Sempre retornamos para 'A' após cada entrega
                        tempo_retorno, 
                        nova_lista_entregas, 
                        entregas_realizadas + [(tempo_inicio, destino, bonus)], 
                        lucro_atual + bonus
                    )

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

    # Variáveis para armazenar o melhor resultado
    max_lucro = 0
    melhor_sequencia = []

    # Iniciar a exploração de todas as combinações possíveis, começando em 'A'
    explorar_entregas('A', 0, entregas, [], 0)

    return {
        "entregas_realizadas": melhor_sequencia,
        "lucro_total": max_lucro
    }