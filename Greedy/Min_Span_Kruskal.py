# Find a minimum span tree given a graph using Kruskal's algorithm

# Function to find root node (parent) of a node in a subtree
def find_parent(parent,i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

edges = [
    ("A", "B", 6),
    ("A", "C", 13),
    ("A", "D", 12),
    ("A", "E", 7),
    ("B", "C", 3),
    ("B", "D", 11),
    ("B", "F", 1),
    ("C", "E", 8),
    ("C", "H", 2),
    ("D", "E", 9),
    ("D", "F", 10),
    ("D", "G", 16),
    ("E", "G", 15),
    ("E", "H", 14),
    ("F", "G", 17),
    ("F", "I", 5),
    ("G", "H", 19),
    ("G", "I", 18),
    ("H", "I", 4)
]
# Sort edges by increasing cost
edges = sorted(edges,key=lambda x:x[2])

# Set nodes to be their own parents
parent = dict()
for u,v,_ in edges:
    parent[u] = u
    parent[v] = v
# Get number of vertices
n_vertices = len(parent)
# Initialize 'rank' of each node to 0, allows to merge subtrees
rank = {elem:0 for elem in parent}
edges_chosen = 0
edge_index = 0
mst = []
while edges_chosen <n_vertices-1:
    # Get node u, node v, and cost w
    u,v,w = edges[edge_index]
    # Get root node in u's subtree
    x = find_parent(parent,u)
    # Get root node in v's subtree
    y = find_parent(parent,v)
    # Check u and v not in same subtree (no cycle)
    if x!=y:
        # Add edge to mst
        mst.append(edges[edge_index])
        edges_chosen +=1
        print(f'Edge count {edges_chosen}:',mst)
        # Merge subtrees by making one root node the parent of the other
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    edge_index +=1
    