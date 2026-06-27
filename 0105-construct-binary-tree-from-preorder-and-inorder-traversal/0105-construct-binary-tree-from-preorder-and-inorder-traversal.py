# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Tracks position in the preorder list and Inorder list
        preIndx = inIndx = 0
        #Defines a DFS recursive function used to build the tree
        def dfs(limit):
            #This allows the function to modify variables defined outside it
            #withou this python will treat it as new local variables
            nonlocal preIndx, inIndx
            #if there are no more nodes to build in preorder, so return None.
            if preIndx >= len(preorder):
                return None
            #This condition checks whether we have finished building the current subtree.
            if inorder[inIndx] == limit:
                #Move to the next position in the inorder list
                inIndx += 1
                #Return None because this subtree is complete
                return None
            #create a root node as the first element is always the rootnode in preorder traversal
            root = TreeNode(preorder[preIndx])
            #After creating the node, move to the next preorder value
            preIndx += 1
            #We recursively build the left subtree.
            root.left = dfs(root.val)
            #Building the right subtree.
            root.right = dfs(limit)
            #After constructing left and right children, return the root of this subtree.
            return root
        #We start recursion with infinite limit
        return dfs(float('inf'))
        