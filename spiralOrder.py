class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        sr=0
        er=n-1
        sc=0
        ec=m-1
        ans = []
        while(sr<=er and sc<=ec):
            for i in range(sc,ec+1):
                ans.append(matrix[sr][i])
            sr+=1

            for i in range(sr,er+1):
                ans.append(matrix[i][ec])
            ec-=1

            if(sr<=er): # To check next row exists or not
                for i in range(ec,sc-1,-1):
                    ans.append(matrix[er][i])
                er-=1

            if(sc<=ec): # To check next column exists or not
                for i in range(er,sr-1,-1):
                    ans.append(matrix[i][sc])
                sc+=1
        return ans
