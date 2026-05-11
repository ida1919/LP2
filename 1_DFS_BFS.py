from collections import deque

g = {
    '1': ['2', '3', '4'],
    '2': ['5', '1',],
    '3': ['5',],
    '4': ['1'],
    '5': [ '6' ],
    '6': ['5']
}

def bfs(start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(g[node])

def dfs(node, visited=None):
    if visited is None:
        visited = set()
    print(node, end=" ")
    visited.add(node)

    for n in g[node]:
        if n not in visited:
            dfs(n, visited)

print("BFS:")
bfs('1')
print("\nDFS:")
dfs('1')