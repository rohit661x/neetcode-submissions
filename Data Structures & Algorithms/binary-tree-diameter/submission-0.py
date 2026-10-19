# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def dfs(node):
            nonlocal diameter

            # Base case: If the node doesn't exist, return 0
            if not node:
                return 0

            # LEFT SUBTREE: Explore completely before moving right
            left = dfs(node.left)

            # Call 1: dfs(1)    → node 1 exists
            # Call 2: dfs(None) → node 1 has no left child, returns 0
            # Call 3: dfs(2)    → right child of node 1
            # Call 4: dfs(3)    → left child of node 2
            # Call 5: dfs(5)    → left child of node 3
            # Call 6: dfs(None) → left child of node 5, returns 0
            # Call 7: dfs(None) → right child of node 5, returns 0

            # RIGHT SUBTREE: Runs after the left subtree finishes
            right = dfs(node.right)

            # Call 8:  dfs(None) → right child of node 3, returns 0
            # Call 9:  dfs(4)    → right child of node 2
            # Call 10: dfs(None) → left child of node 4, returns 0
            # Call 11: dfs(None) → right child of node 4, returns 0
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return diameter