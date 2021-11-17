# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(node: TreeNode) -> list[int]:
            if not node:
                return [None]
            visited = []
            visited.append(node.val)
            if node.left or node.right:
                visited += preorder(node.left)
                visited += preorder(node.right)
            return visited

        def postorder(node: TreeNode) -> list[int]:
            if not node:
                return [None]
            visited = []
            if node.left or node.right:
                visited += postorder(node.left)
                visited += postorder(node.right)
            visited.append(node.val)
            return visited

        left = preorder(root.left)
        right = postorder(root.right)
        right.reverse()
        return left == right
