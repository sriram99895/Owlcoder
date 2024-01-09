#         self.right = right
# leaf are equal or not
class Solution:
    def Inorder(self,root,l):
        if root:
            self.Inorder(root.left,l)
            if root.left == None and root.right == None:
                l.append(root.val)
            self.Inorder(root.right,l)
        return l        

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l = self.Inorder(root1,[])
        p = self.Inorder(root2,[])
        # print(l)
        # print(p)
        if len(l) == len(p):
            for i in range(len(p)):
                if l[i] != p[i]:
                    return 0
            return 1
        return 0  