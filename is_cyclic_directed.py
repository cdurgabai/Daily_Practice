def has_cycle_dfs(node, adj, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            if has_cycle_dfs(neighbor, adj, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False

def is_cyclic_directed(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * (n + 1)
    rec_stack = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            if has_cycle_dfs(i, adj, visited, rec_stack):
                return True
    return False

t = int(input())
for _ in range(t):
    n, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    print(is_cyclic_directed(n, edges))
