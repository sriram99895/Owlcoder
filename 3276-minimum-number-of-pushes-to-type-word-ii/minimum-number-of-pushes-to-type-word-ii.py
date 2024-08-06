class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for i in word:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        k = list(d.values())
        k.sort()
        k.reverse()
        j = 0
        s = 0
        c =0
        for i in k:
            if c%8 == 0:
                j+=1
            s+=i*j
            c+=1
        return s
           
        