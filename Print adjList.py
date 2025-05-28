# Generate/Print adjList
def printGraph(V,E,edges):
    adjList=[]
    for i in range(V):
        adjList.append([])
    for n,m in edges:
        adjList[n].append(m)
        adjList[m].append(n)
    for lst in adjList:
        lst.sort()
    return adjList
V=5
E=7
edges=[[0,1],[0,4],[1,4],[1,3],[1,2],[4,3],[3,2]]
print(printGraph(V,E,edges))
# o/p: [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]]
