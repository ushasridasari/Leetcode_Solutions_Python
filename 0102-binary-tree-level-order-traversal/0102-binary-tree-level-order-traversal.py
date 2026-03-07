# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #if root is emplty returns empty list
        if not root:
            return []
        #Creates a list to store all levels of the tree
        res = []
        #Initializes a queue with the root node to start BFS traversal.
        queue = deque([root])
        #loop runs until the queue becomes empty.
        while queue:
            #Creates a list to store nodes of the current level.
            level = []
            #len(queue) gives the number of nodes in the current level
            for i in range(len(queue)):
                #Removes the first node from the queue
                node = queue.popleft()
                #checking if there is a node
                if node:
                    #Add the node value to curent level list
                    level.append(node.val)
                    #Add left child to the queue.
                    queue.append(node.left)
                    #Add right child to the queue.
                    queue.append(node.right)
            #Add level to result
            if level:
                res.append(level)
        return res
            
            
        