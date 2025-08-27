from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        num_nodes = len(graph)
        all_visited_mask = (1 << num_nodes) - 1
        q = deque()

        # visited[mask][node] = True if we've been at 'node' with 'mask' visited
        visited = [[False] * num_nodes for _ in range(all_visited_mask + 1)]

        # Initialize queue with all starting nodes
        for node in range(num_nodes):
            mask = 1 << node
            q.append((node, mask, 0))  # start with distance 0
            visited[mask][node] = True

        while q:
            node, mask, dist = q.popleft()
            if mask == all_visited_mask:
                return dist

            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if not visited[next_mask][neighbor]:
                    visited[next_mask][neighbor] = True
                    q.append((neighbor, next_mask, dist + 1))

        return -1  # Shouldn't happen if the graph is connected
