# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if there is no root then tree doesnot exists so return none
        if not root:
            return None
        #assign the left node to right and right node to left
        root.left, root.right = root.right, root.left
        #Recursively calls the invertTree function on the left child of the current node
        self.invertTree(root.left)
        #Recursively calls the invertTree function on the right child of the current node
        self.invertTree(root.right)
        #returning the modified root
        return root

        #TC: O(n)
        #SC: O(n)
        