# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #def dfs(node,arr[]):
        def dfs(node,arr):
            if not node:
                arr.append(None)
                return 
            
            #arr.append(node)
            arr.append(node.val)
            dfs(node.left,arr)
            dfs(node.right,arr)

        if not p and not q:
            return True
        t1=[]
        t2=[]
        dfs(p,t1)
        dfs(q,t2)
        return t1==t2
