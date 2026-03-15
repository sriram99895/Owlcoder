class Solution:
    def convert(self, s: str, numRows: int) -> str:
        st = ""
        cycle = 2*(numRows-1)
        print(numRows,cycle)
        if numRows == 1:
            return s
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                ind = i
                while ind<len(s):
                    st+=s[ind]
                    ind+=cycle
            else:
                ind = i
                c = 0
                while ind < len(s):
                    st+=s[ind]
                    if c == 0:
                        ind += cycle-2*(i)
                        c = 1
                    else:
                        ind += 2*i
                        c = 0


        return st            



        