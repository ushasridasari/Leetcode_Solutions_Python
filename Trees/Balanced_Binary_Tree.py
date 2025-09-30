# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #function 
        def dfs(root):
            # if no root, tree is balanced
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # left and right subtree is balanced and absolute value of the height difference between left and right
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return [isBalanced, height of this subtree]
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
