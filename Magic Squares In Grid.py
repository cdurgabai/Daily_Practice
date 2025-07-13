class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            nums = [grid[i+x][j+y] for x in range(3) for y in range(3)]
            if sorted(nums) != list(range(1, 10)):
                return False
            rows = [sum(grid[i+k][j:j+3]) for k in range(3)]
            cols = [sum(grid[i+k][j+x] for k in range(3)) for x in range(3)]
            diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
            return all(s == 15 for s in rows + cols + [diag1, diag2])
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if grid[i+1][j+1] == 5 and isMagic(i, j):
                    count += 1
        return count
