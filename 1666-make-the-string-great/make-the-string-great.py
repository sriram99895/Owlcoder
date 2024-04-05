class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i.isupper():
                if i.lower() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)    
            elif i.islower():
                if i.upper() == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)    
            else:
                stack.append(i)
        return "".join(stack)                  
