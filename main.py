import heapq

# ==========================================
# TAREFA 1: Representar o fluxo como grafo
# ==========================================
# Os pesos representam o "esforço" ou "tempo em dias" para passar de uma etapa a outra.
# Menor custo = fluxo mais eficiente.
crm_grafo = {
    'Lead': {'Contato Inicial': 1, 'Reuniao': 5}, # Tentar pular o contato e ir para reunião direto custa mais
    'Contato Inicial': {'Reuniao': 2, 'Proposta': 4},
    'Reuniao': {'Proposta': 1},
    'Proposta': {'Negociacao': 2, 'Confirmacao': 6}, # Forçar a confirmação direto da proposta é difícil
    'Negociacao': {'Confirmacao': 1},
    'Confirmacao': {} # Fim do fluxo
}

# ==========================================
# TAREFA 2: Implementar o algoritmo de Dijkstra
# ==========================================
def dijkstra(grafo, inicio, fim):
    # Dicionário para armazenar o menor custo para chegar a cada nó
    custos = {no: float('inf') for no in grafo}
    custos[inicio] = 0
    
    # Dicionário para rastrear o caminho (de onde viemos para chegar no nó atual)
    caminho_anterior = {no: None for no in grafo}
    
    # Fila de prioridade para explorar os nós com menor custo primeiro
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)
        
        # Se chegamos ao destino, podemos parar
        if no_atual == fim:
            break
            
        # Se encontrarmos um custo maior do que o já registrado, ignoramos
        if custo_atual > custos[no_atual]:
            continue
            
        # Analisar os vizinhos do nó atual
        for vizinho, peso in grafo[no_atual].items():
            novo_custo = custo_atual + peso
            
            # Se encontrarmos um caminho mais barato para o vizinho
            if novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                caminho_anterior[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
                
    # Reconstruir o menor caminho
    caminho = []
    no_passo = fim
    while no_passo is not None:
        caminho.append(no_passo)
        no_passo = caminho_anterior[no_passo]
        
    caminho.reverse() # Inverter para mostrar do Início ao Fim
    
    return caminho, custos[fim]

# Executando a função
origem = 'Lead'
destino = 'Confirmacao'
melhor_caminho, custo_total = dijkstra(crm_grafo, origem, destino)

print("--- RESULTADOS DO CRM ---")
print(f"Grafo do CRM: {list(crm_grafo.keys())}")
print(f"Melhor caminho de {origem} para {destino}: {' -> '.join(melhor_caminho)}")
print(f"Custo total (esforço/dias): {custo_total}")