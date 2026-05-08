"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            #Checks if the node is already copied
            if node in oldToNew:
                #return the existing copy, do not create a new one
                return oldToNew[node]
            #Creates a new node with the same value
            copy = Node(node.val)
            #Stores mapping between original node and copied node.
            oldToNew[node] = copy
            #Loops through all neighbors of the current node.
            for nei in node.neighbors:
                #Clone the neighbor using DFS, and adding the cloned neighbor to current copied node
                copy.neighbors.append(dfs(nei))
            #Returns the fully cloned node
            return copy
        #It checks whether node exists or not.If node is not None → True, If node is None → False
        return dfs(node) if node else None
    
#TC: O(V+E)
#SC: O(V)
        