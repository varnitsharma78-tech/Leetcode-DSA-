# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base Case 1: Both nodes are None -> structurally identical so far
        if not p and not q:
            return True
        
        # Base Case 2: One node is None and the other is not -> structural mismatch
        if not p or not q:
            return False
        
        # Base Case 3: The values of the current nodes do not match
        if p.val != q.val:
            return False
        
        # Recursively check if the left subtrees and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
