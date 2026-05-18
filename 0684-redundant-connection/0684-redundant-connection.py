class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Stores total number of edges.
        n = len(edges)
        #Creates an empty graph and Nodes start from 1, not 0. so we use n+1
        adj = [[] for i in range(n + 1)]
        #Loops through every edge.
        for u, v in edges:
        #Adding connections between nodes
            #Adds v as neighbor of u.
            adj[u].append(v)
            #Adds u as neighbor of v.
            adj[v].append(u)
        #Tracks visited nodes initially it will be [False, False, False, False]
        visit = [False] * (n + 1)
        #Create Cycle Set to store nodes belonging to cycle
        cycle = set()
        #Create Cycle Start, Stores where cycle begins, -1 means has cycle not started.
        cycleStart = -1

        #DFS explores graph deeply, node = curr node, par = parent node
        def dfs(node, par):
            #Allows DFS to change outer variable.
            nonlocal cycleStart
            #If node already visited
            if visit[node]:
                #Stores where cycle started
                cycleStart = node
                #Cycle found
                return True
            #Mark node as visited
            visit[node] = True
            #Loops through neighboring nodes.
            for nei in adj[node]:
                #Skips parent node
                if nei == par:
                    continue
                #Explore neighbor nodes
                if dfs(nei, node):
                    #Adds nodes inside cycle.
                    if cycleStart != -1:
                        cycle.add(node)
                    #if node Reached Cycle Start
                    if node == cycleStart:
                        #Stop Collectiog ccyle nodes
                        cycleStart = -1
                    #Continue sending cycle info upward
                    return True
            #No Cycle found 
            return False
        #Starts DFS from node 1 which has no parent(-1)
        dfs(1, -1)

        #Checks edges from LAST to FIRST
        for u, v in reversed(edges):
            #If both nodes belong to cycle,  # because problem asks for last edge causing cycle
            if u in cycle and v in cycle:
                #Returns redundant edge.i.e, extra edge
                return [u, v]

        return []

#TC: O(V+E)
#SC: O(V+E)

# Where V is the number of vertices and E is the number of edges in the graph.