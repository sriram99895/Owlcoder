class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        d = {}
        # if len(trust) == 0:
        #     return 1
        print(trust)
        for i in trust:
            if i[1] not in d:
                d[i[1]] = 1
            else:
                d[i[1]]+=1
        for i in trust:
            if i[0] in d:
                d[i[0]]-=1
        print(d)                
        for k,v in d.items():
            if v == n-1:
                return k  
        if n == 1 and len(d) == 0:
            return 1
        return -1   