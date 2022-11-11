from collections import defaultdict
from heapq import *

with open('graph.txt','r') as f:
    lines = f.readlines()
edges = []
for line in lines:
    edge = line.split(' ')
    edges.append((edge[0],edge[1],int(edge[2])))

graph = defaultdict(list)
for left,right,cost in edges:
    graph[left].append((cost,right))
    graph[right].append((cost,left))

def dijkstra(graph,start,finish):
    q = [(0, start, [])]
    seen = set()
    mins = {start: 0}
    while(q):
        (total_cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = path + [v1]
            if v1 == finish:
                return (total_cost,path)
            for cost,v2 in graph.get(v1,()):
                if v2 in seen:
                    continue
                prev = mins.get(v2,None)
                next = total_cost + cost
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q,(next,v2,path))
    return (float('inf'),[])
for key in graph:
    cost,path = dijkstra(graph,'A',key)
    print(f'{key}:\ncost: {cost}, path: {path}')