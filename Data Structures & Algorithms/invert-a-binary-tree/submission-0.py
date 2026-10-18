# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #binary tree
        # return inverted tree from root -> swap L & R children
        # DFS or BFS? DFS: Recursion or stack / BFS queue
            #The operation at each node is identical: swap its children  and apply to both subtrees.
            #This naturally fits recursion. -> DFS Recursion
        
        if not root:
            return None
        #now given a root is valid

        root.left, root.right = root.right, root.left
        #swap left and right values

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root