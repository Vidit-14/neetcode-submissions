# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def postOrder(node):
            nonlocal res
            
            if not node:
                return 0
            
            leftMax = postOrder(node.left)
            rightMax = postOrder(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res = max(res, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        postOrder(root)
        return res