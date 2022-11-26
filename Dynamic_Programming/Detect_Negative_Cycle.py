# Detect negatice cycle in graph
edges = {
    'a':[('b',6),('t',0)],
    'b':[('c',2),('d',18),('t',0)],
    'c':[('a',-11),('d',-23),('t',0)],
    'd':[('t',0)],
    'e':[('d',5),('c',-15),('t',0)],
}
nodes = ['t','a','b','c','d','e']
opt = {node:[(float('inf'),'') for _ in range(len(nodes)+1)] for node in nodes}
opt['t'][0] = (0,'')

min_val = float('inf')
for i in range(1,len(nodes)+1):
    for node in nodes:
        opt[node][i] = opt[node][i-1]
        for edge in edges.get(node,[]):
            if opt[node][i][0]>opt[edge[0]][i-1][0]+edge[1]:
                opt[node][i] = [opt[edge[0]][i-1][0]+edge[1],edge[0]+opt[edge[0]][i-1][1]]

for node in opt:
    print(node,' '.join([f'{str(elem):15s}' for elem in opt[node]]))