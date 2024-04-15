# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def su(self,root:Optional[TreeNode],s,l):
        if root:
            if root.left == None and root.right == None:
                # print(s)
                l.append(int(s+str(root.val)))
                return
            s+=str(root.val)
            self.su(root.left, s,l)
            self.su(root.right,s,l)
        return l 

           

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return root.val
        k = self.su(root,"",[])
        return sum(k)
        