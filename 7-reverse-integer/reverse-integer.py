class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x=sign*x
        x = str(x)
        x=x[::-1]
        x=sign*(int(x))
        return 0 if x<(-(2**31)) or x>((2**31)-1) else x
        