# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Creates an empty list to store all node values in sorted order.
        arr = []
        #Defines a recursive function dfs to traverse the tree
        def dfs(node):
            #If the node is None, stop recursion
            if not node:
                return 0
            #Traverse Left Subtree i.e, first explore the entire left subtree
            dfs(node.left)
            #After finishing the left side, visit the current node and store its value in arr
            arr.append(node.val)
            #move to the right subtree
            dfs(node.right)
        #Start the DFS traversal from the root of the tree.
        dfs(root)
        #Returning the kth element
        return arr[k-1]

        #TC: O(n)
        #SC: O(n)
        


