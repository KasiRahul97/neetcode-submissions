# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def height(root):
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            h=1+max(l,r)
            return h
        def diam(root):
            if not root:
                return 
            left=height(root.left)
            right=height(root.right)
            self.res=max(self.res,left+right)
            diam(root.left)
            diam(root.right)
        diam(root)
        return self.res