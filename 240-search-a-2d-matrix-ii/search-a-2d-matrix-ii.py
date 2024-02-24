class Solution:
    def searchMatrix(self, l: List[List[int]], target: int) -> bool:
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j] == target:
                    return 1
        return 0            
        