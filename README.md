# Sprint 4 — Grafos e Dijkstra no CRM

## 👥 Integrantes do Grupo
* **Davi Correa Paião** - RM: 560438
* **Marcos Vinicius Gonçalves Santos** - RM: 560062
* **Matheus Ricardo Parreira da Silva** - RM: 560099

## 🎯 Objetivo
Modelar o fluxo de um CRM (Customer Relationship Management) como um grafo direcionado e utilizar o algoritmo de Dijkstra para encontrar o caminho mais eficiente (menor custo/tempo) entre a entrada de um `Lead` e a `Confirmação` da venda.

## 🚀 Tarefas Realizadas
1. **Representação em Grafo:** O fluxo de vendas foi mapeado com etapas interconectadas, onde as arestas possuem pesos que representam o nível de dificuldade ou tempo em dias para avançar de uma fase a outra.
2. **Implementação do Algoritmo:** Criamos a função `dijkstra` em Python, utilizando a biblioteca `heapq` (fila de prioridade) para calcular as rotas mais baratas.
3. **Análise de Eficiência:** A saída do código provou que o caminho passo a passo pelo funil de vendas tem menor resistência do que tentar "pular" etapas fundamentais.

## 💻 Como rodar o projeto
Pré-requisitos: Ter o [Python 3.x](https://www.python.org/) instalado em sua máquina.

1. Clone o repositório ou baixe o arquivo `main.py`.
2. Abra o terminal e navegue até a pasta do arquivo.
3. Execute o comando:
   ```bash
   python main.py
