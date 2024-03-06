class Solution:
    def removeElement(self, l: List[int], v: int) -> int:
        c=0
        for i in l:
            if i==v:
                c+=1
        for i in range(c):
            l.remove(v)
        return len(l)            