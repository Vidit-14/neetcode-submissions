# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        currMax = float('-inf')
        stack = []
        stack.append((root, currMax))
        count = 0

        while stack:
            node, currMax = stack.pop()
            if node.val >= currMax:
                count += 1
                currMax = node.val
            
            if node.right:
                stack.append((node.right, currMax))
            if node.left:
                stack.append((node.left, currMax))
        
        return count
        