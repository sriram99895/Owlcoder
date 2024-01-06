    def count(int n):    
        i = 0
        s = 0
        n = n+1
        while 2**i<=n:
            b = ((n)//(2**(i+1)))*(2**i)
            r = ((n)%(2**(i+1)))
            if r>=(2**i):
                k = ((n)%(2**(i+1)))%(2**i)
                s+=k
            s+=b
            i+=1
        return s  
n = int(input())
print(count(n))        