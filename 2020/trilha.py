#InterIF 2020 - Fase Única
#Problema K - Trilha de Amigos

def dijkstra(graph, start, goal):
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  unvisited_nodes = list(graph.keys())
  previous_nodes = {node: None for node in graph}

  while unvisited_nodes:
    current_node = min(unvisited_nodes, key=lambda node: distances[node])
    unvisited_nodes.remove(current_node)

    if distances[current_node] == float('inf'): break

    for neighbor, weight in graph[current_node]:
      distance = distances[current_node] + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        previous_nodes[neighbor] = current_node

  path = []
  while goal:
    path.append(goal)
    goal = previous_nodes[goal]
  path.reverse()

  return path

N, M = [int(i) for i in input().split()]
start, end = input().split()
graph = {}
for i in range(M):
  edge = input().split()
  if edge[0] not in graph: graph[edge[0]] = []
  if edge[1] not in graph: graph[edge[1]] = []
  graph[edge[0]].append((edge[1], int(edge[2])))
  graph[edge[1]].append((edge[0], int(edge[2])))

print("Percurso:", "--> ".join(dijkstra(graph, start, end)))
