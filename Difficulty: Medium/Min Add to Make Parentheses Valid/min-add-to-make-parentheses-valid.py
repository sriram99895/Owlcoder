class Solution:
    def minParentheses(self, s):
        # code here
        stack = []
        for i in s:
            if i=="(":
                stack.append(i)
            elif i ==')':
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)                
        