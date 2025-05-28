# DFS in Graphs
class Solution:
    def dFS(self,Node,visited,adj,ans):
        visited[Node]=1
        ans.append(Node)
        for it in adj[Node]:
            if(visited[it]==0):
                self.dFS(it,visited,adj,ans)
    def dfs(self,adj):
        v=len(adj)
        ans=[]
        visited=[0]*v
        Node=0 #Connected components
        """
        # Unconnceted components
        for i in range(0,v):
            if(visited[i]==0):
                self.dFS(i,visited,adj,ans)
        """
        if visited[Node]==0:
            self.dFS(Node,visited,adj,ans)
        return ans

# v, e = map(int, input().split())
# adj = [[] for _ in range(v)]
# for _ in range(e):
#     u, w = map(int, input().split())
#     adj[u].append(w)
#     adj[w].append(u) 

adj=[[2, 3, 1], [0], [0, 4], [0], [2]]
s=Solution()
res=s.dfs(adj)
print(res)
#adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]] --> o/p: [0, 2, 4, 3, 1]
