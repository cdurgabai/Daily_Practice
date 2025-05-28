# Number of Islands
# 1-> Land and 0-> Water
def dfs(i,j,visited,grid,n,m):
    visited[i][j]=1
    for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
        delRow=i+row
        delCol=j+col
        if(delRow>=0 and delRow<n and delCol>=0 and delCol<m and grid[delRow][delCol]=="1" and visited[delRow][delCol]==0):
            dfs(delRow,delCol,visited,grid,n,m)
def numIslands(grid):#List[List[str]])-> int:
    n=len(grid)
    m=len(grid[0])
    visited=[]
    for i in range(n):
        temp=[0]*m
        visited.append(temp)
    count=0   
    for i in range(n):
        for j in range(m):
            if(grid[i][j]=='1' and visited[i][j]==0):
                dfs(i,j,visited,grid,n,m)
                count+=1
    return count

def main():
    n, m = map(int, input().split())
    grid = [input().split() for _ in range(n)]
    print(numIslands(grid))

if __name__ == "__main__":
    main()

"""
i/p:
4 4
1 1 0 1
1 1 0 0
0 0 0 0 
1 0 0 1
o/p: 4
"""
