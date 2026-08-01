# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val

        def inorderDFS(node):
            nonlocal count, res #access enclosing scope variable
            
            if not node: return

            inorderDFS(node.left)
            if count == 0: return
            
            count -= 1

            if count == 0:
                res = node.val
                return
            
            inorderDFS(node.right)

        inorderDFS(root)
        return res

