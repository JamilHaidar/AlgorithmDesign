network = [[0, 10, 10, 0, 0, 0],
        [0, 0, 2, 4, 8, 0],
        [0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 6, 0, 10],
        [0, 0, 0, 0, 0, 0]]
n = len(network)

def bfs(s,t,parent):
    visited = [False]*n
    queue = [s]
    visited[s] = True
    while queue:
        node = queue.pop(0)
        for neighbor,capacity in enumerate(network[node]):
            if not visited[neighbor] and capacity>0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = node
                if neighbor==t:return True
    return False

source = 0
sink = 5
parent = [-1]*n
max_flow = 0
iter = 0
while bfs(source,sink,parent):
    iter +=1
    print(f'\n\nIteration: {iter}\n==============\n')
    print('Current Graph:')
    print(' ',' '.join([f'{str(i):5s}' for i in range(n)]))
    for node,edges in enumerate(network):
        print(node,' '.join([f'{str(i):5s}' for i in edges]))

    path_flow = float('inf')
    temp_node = sink
    found_path = []
    while temp_node!=source:
        found_path.append(temp_node)
        path_flow = min(path_flow,network[parent[temp_node]][temp_node])
        temp_node = parent[temp_node]
    found_path.append(temp_node)
    max_flow += path_flow
    
    print(f'\nPath flow: {path_flow}, Max flow: {max_flow}')
    print(f'Path found: {"->".join([str(elem) for elem in found_path[::-1]])}')

    v = sink
    while v!=source:
        u = parent[v]
        network[u][v] -=path_flow
        network[v][u] +=path_flow
        v = parent[v]

print(max_flow)