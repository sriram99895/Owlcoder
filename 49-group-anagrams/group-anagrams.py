class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d = {}
        # for i in s:
        #     print(i)
        for i in s:
            k = "".join(sorted(i))
            if k not in d:
                d[k] = [i]
            else:
                d[k].append(i)
        l = []
        for v in d.values():
            l.append(v)
        return l            


        
        