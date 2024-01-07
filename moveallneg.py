#move all negative elements to end
class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        l = []    
        for i in arr:
            if i > 0:
                l.append(i)
        for i in arr:
            if i<0:
                l.append(i)
        arr.clear()
        for i in l:
            arr.append(i)
        return arr    
arr = list(map(int,input().split()))
Solution k
l = k.segregateElements(arr)
print(l)
