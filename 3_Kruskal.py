
edges = [
    (0,1,4),
    (1,2,2),
    (0,3,3),
    (3,4,7),
    (4,5,9),
    (4,2,5),
    (2,5,6)
]

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = list(range(n))

    print("Edges in MST:")

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            print(u, "-", v, ":", w)
            parent[x] = y



kruskal(edges, 6)
