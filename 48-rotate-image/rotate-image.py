class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        h=[]
        for j in range(n):
            p=[]
            for i in range(n-1,-1,-1):
                p.append(matrix[i][j])
            h.append(p)    
        for i in range(n):
            for j in range(n):
                matrix[i][j]=h[i][j]