# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #right>root>left
        #If the tree has no nodes, returns true
        if not root:
            return True
        #This creates a queue i.e, (node=root, min=-∞, max=+∞)
        q = deque([(root, float("-inf"), float("inf"))])
        #Loop runs until all nodes are checked
        while q:
            #Removes the first element from the queue.
            node, left, right = q.popleft()
            #Verifies the conditon
            if not (left < node.val < right):
                return False
            #If the node has a left child, add it to the queue.
            if node.left:
                q.append((node.left, left, node.val))
            #If the node has a left child, add it to the queue.
            if node.right:
                q.append((node.right, node.val, right))

        return True

        #TC and SC: O(n)
            
        