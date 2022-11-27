from collections import defaultdict

network = {
    's':{'2':10,'3':10},
    '2':{'3':2,'4':4,'5':8},
    '3':{'5':9},
    '4':{'t':10},
    '5':{'4':6,'t':10}
}
nodes = ['s','2','3','4','5','t']

for elem in network:
    network[elem] = defaultdict(int,network[elem])
network = defaultdict(lambda: defaultdict(int),network)

n = len(network)
def bfs(s,t,parent):
    visited = {node:False for node in nodes}
    queue = [s]
    visited[s] = True
    while queue:
        node = queue.pop(0)
        for neighbor in network[node]:
            capacity = network[node][neighbor]
            if not visited[neighbor] and capacity>0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = node
                if neighbor==t:return True
    return False

source = 's'
sink = 't'
parent = {node:node for node in nodes}
max_flow = 0
iter = 0
while bfs(source,sink,parent):
    iter +=1
    print(f'\n\nIteration: {iter}\n==============\n')
    print('Current Graph:')
    for node in network:
        print(node,dict(network[node]))

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