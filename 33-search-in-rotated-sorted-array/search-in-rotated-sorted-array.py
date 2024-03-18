class Solution:
    def search(self, l: List[int], target: int) -> int:
        if target in l:
            return l.index(target)
        else:
            return -1  
        