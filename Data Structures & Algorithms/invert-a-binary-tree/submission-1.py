# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        
        stack.append(root)

        while stack:
            cur = stack.pop()
            if cur and cur.left and cur.right:
                stack.append(cur.left)
                stack.append(cur.right)

                temp = cur.left
                cur.left = cur.right
                cur.right = temp
            elif cur and not cur.left:
                stack.append(cur.right)
                cur.left = cur.right
                cur.right = None
            elif cur and not cur.right:
                stack.append(cur.left)
                cur.right = cur.left
                cur.left = None
            else:
                continue

        return root            