# Find minimum cost path in graph with negative edges
import collections
edges = {
    'a':[('b',-4),('t',-3)],
    'b':[('d',-1),('e',-2)],
    'c':[('b',8),('t',3)],
    'd':[('a',6),('t',4)],
    'e':[('c',-3),('t',2)],
}
inverted_edges = collections.defaultdict(list)
for v in edges:
    for w in edges[v]:
        inverted_edges[w[0]].append((v,w[1]))

nodes = ['t','a','b','c','d','e']
opt = {node:float('inf') for node in nodes}
successor = {node:None for node in nodes}
opt['t'] = 0
successor['t'] = 't'
active = {'t'}
while active:
    node = active.pop()
    for edge in inverted_edges.get(node,[]):
        if opt[edge[0]]>opt[node]+edge[1]:
            opt[edge[0]] = opt[node]+edge[1]
            successor[edge[0]] = node
            active.add(edge[0])

for node in opt:
    print(node,opt[node])

start_node = min([(opt[node],node) for node in opt])
print(f'Minimum path cost: {start_node[0]}')
path = []
start_node = start_node[1]
while start_node!='t':
    path.append(start_node)
    start_node = successor[start_node]
path.append('t')
print('Path','->'.join(path))