# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Creates an empty list res to store the values of nodes visible from the right side
        res = []
        #Defines a function
        def dfs(node, depth):
            #checks if the current node is null
            if node == None:
                #Stops recursion.
                return []
            #checks if this is the first node visited at this depth level.
            if depth == len(res):
                #Adds the node value to res
                res.append(node.val)
            #Recursively visits the right child first and increases the depth by 1
            dfs(node.right, depth + 1)
            #Recursively visits the left child after the right child
            dfs(node.left, depth + 1)
        #Starts the DFS traversal from the root node at depth 0
        dfs(root, 0)
        #Returns the list containing the right side view of the tree.
        return res

        #TC: O(n)
        #SC: O(n)
        