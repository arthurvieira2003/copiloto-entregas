def processar_entregas(conexoes, entregas):
    matriz_conexoes = {}
    for origem, destino, tempo in conexoes:
        if origem not in matriz_conexoes:
            matriz_conexoes[origem] = {}
        matriz_conexoes[origem][destino] = tempo

    lucro_total = 0
    tempo_atual = 0
    entregas_realizadas = []

    for entrega in entregas:
        tempo_saida, destino, bonus = entrega
        if destino in matriz_conexoes['A']:
            tempo_viagem = matriz_conexoes['A'][destino]
            tempo_retorno = tempo_viagem
            tempo_total = tempo_viagem + tempo_retorno
            
            if tempo_atual + tempo_total <= tempo_saida:
                tempo_atual += tempo_total
                lucro_total += bonus
                entregas_realizadas.append(entrega)

    return {
        "entregas_realizadas": entregas_realizadas,
        "lucro_total": lucro_total
    }
