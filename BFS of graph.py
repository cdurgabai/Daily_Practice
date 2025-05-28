# BFS of graph
class Solution:
    def bfs(self, adj):
        v=len(adj)
        visited=[0]*v
        startNode=0
        q=[]
        ans=[]
        if visited[startNode]==0:
            visited[startNode]=1
            q=[startNode]
            while q:
                node=q.pop(0)
                ans.append(node)
                for i in adj[node]:
                    if visited[i]==0:
                        visited[i]=1
                        q.append(i)
        return ans
