def has_cycle_dfs(adj, visited, node, parent):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if has_cycle_dfs(adj, visited, neighbor, node):
                return True
        elif neighbor != parent:
            return True
    return False

def is_cyclic(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            if has_cycle_dfs(adj, visited, i, -1):
                return True
    return False

t = int(input())
for _ in range(t):
    n, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    print(is_cyclic(n, edges))
