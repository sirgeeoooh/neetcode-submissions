# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        
        while queue:
            rightMostNode = None
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    rightMostNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightMostNode:
                res.append(rightMostNode.val)
        
        return res