class Solution:
    def evalRPN(self, a: List[str]) -> int:
        s = []
        for i in a:
            if i == "+":
                a= s.pop()
                b = s.pop()
                k = a+b
                s.append(k)
            elif i == "-":
                a= s.pop()
                b = s.pop()
                k =b-a
                s.append(k)
            elif i == "*":
                a= s.pop()
                b = s.pop()
                k = a*b
                s.append(k)
            elif i=="/":
                a= s.pop()
                b = s.pop()
                if a< 0 and b<0:
                    k = abs(b)//abs(a)
                    s.append(k)
                elif a<0 or b<0:
                    sign = -1
                    k = sign*(abs(b)//abs(a))
                    s.append(k)
                else:
                    k = b//a
                    s.append(k)    

            else:
                s.append(int(i)) 
        # print(s)    
        return s[0]
        