from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # ToDo: Write Your Code Here.
        # Creates a list where each node initially has no incoming edge.
        visited = [False] * n
        # Creates an empty list to store starting nodes.
        result = []
        adjList = [[] for _ in range(n)]
        #Processes every directed edge from u to v.
        for u, v in edges:
            adjList[u].append(v)
            # Marks v as true because it has an incoming edge from u.
            visited[v] = True
        for i in range(n):
            # Checks whether node i has no incoming edge.
            if not visited[i]:
                # Adds node i because it must be an initial node.
                result.append(i)

        return result

