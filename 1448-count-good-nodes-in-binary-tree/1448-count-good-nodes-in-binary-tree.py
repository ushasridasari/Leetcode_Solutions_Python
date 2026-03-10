# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Creates a variable res to store the count of good nodes
        res = 0
        #Creates a queue using deque for BFS traversal.
        q = deque()

        q.append((root,-float('inf')))
        #Runs the loop until the queue becomes empty
        while q:
            #Removes the first element from the queue
            node,maxval = q.popleft()
            #checks whether the current node value is greater than or equal to the maximum value seen so far
            if node.val >= maxval:
                #Increases the good node count by 1
                res += 1
            #Checks if the current node has a left child
            if node.left:
                #Adds the left child to the queue and updates the maximum value seen so far
                q.append((node.left,max(maxval,node.val)))
            #Checks if the current node has a right child
            if node.right:
                #Adds the left child to the queue and updates the maximum value seen so far
                q.append((node.right,max(maxval,node.val)))

        return res 

        #TC: O(n)
        #SC: O(n)
