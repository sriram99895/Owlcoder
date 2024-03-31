import sys
class Solution:
    def removeKdigits(self, st: str, k: int) -> str:
        sys.set_int_max_str_digits(100000)
        if len(st) == 1 and k == 1:
            return "0"
        c = 0
        s = []
        f = 0
        for i in range(len(st)):
            if len(s) == 0:
                s.append(st[i])
            elif len(s) > 0 and int(s[-1]) > int(st[i]) and c < k :
                while len(s)>0 and int(s[-1]) > int(st[i]):
                    s.pop()
                    # print(s)
                    c+=1
                    if c == k:
                        break 
                s.append(st[i])        
            else:
                s.append(st[i])
        while len(s)>0 and c<k:
            s.pop()
            c+=1        
        p = ""
        if len(s) == 0:
            return "0"
        for i in s:
            p+=i
        # print(int(p)) 
        p = int(p)
        return str(p)
        