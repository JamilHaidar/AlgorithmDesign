# Find minimum cost path in graph with negative edges
edges = {
    'a':[('b',-4),('t',-3)],
    'b':[('d',-1),('e',-2)],
    'c':[('b',8),('t',3)],
    'd':[('a',6),('t',4)],
    'e':[('c',-3),('t',2)],
}
nodes = ['t','a','b','c','d','e']
opt = {node:[(float('inf'),'') for _ in range(len(nodes))] for node in nodes}
opt['t'][0] = (0,'')

for i in range(1,len(nodes)):
    for node in nodes:
        opt[node][i] = opt[node][i-1]
        for edge in edges.get(node,[]):
            if opt[node][i][0]>opt[edge[0]][i-1][0]+edge[1]:
                opt[node][i] = [opt[edge[0]][i-1][0]+edge[1],edge[0]+opt[edge[0]][i-1][1]]
print(' ',' '.join([f'{str(i):12s}' for i in range(len(nodes))]))
for node in opt:
    print(node,' '.join([f'{str(elem):12s}' for elem in opt[node]]))