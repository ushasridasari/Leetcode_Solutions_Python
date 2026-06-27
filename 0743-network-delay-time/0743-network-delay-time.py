class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Creates adjacency list to stores neighbors
        adj = defaultdict(list)
        #Loops through every edges where u is source node, v is destination node & w is the traveltime
        for u, v, w in times:
            #Store neighbor and weight ie, {2: [(1,1), (3,1)], 3: [(4,1)]}
            adj[u].append((v,w))
        #initially every node distance = infinity 
        dist = {node: float("inf") for node in range(1, n+1)}
        #Defines DFS function with current node and current total travel time.
        def dfs(node, time):
            #Checks if this path is slower than an already known path.
            if time >= dist[node]:
                #Stops DFS because this path is not useful.
                return
            #Updates the shortest known time for the current node.
            dist[node] = time
            #if there are no neighbor nodes
            if not adj[node]:
                #stop for looking neighbors
                return
            #Loops through all neighbors of the current node.
            for nei, w in adj[node]:
                #Recursively visits the neighbor with updated total time.
                dfs(nei, time + w)
        #Starts DFS from node k with time 0.
        dfs(k, 0)
        #Finds the maximum time among all shortest distances.
        res = max(dist.values())
        #Returns the answer if all nodes are reachable, otherwise returns -1.
        return res if res < float('inf') else -1

#TC: O(V+E)
#SC: O(V+E)

# Where V is the number of vertices and E is the number of edges in the graph.