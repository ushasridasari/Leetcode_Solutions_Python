class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #number of points, start from point 0
        n, node = len(points), 0
        #smallest cost needed to connect each point. Initially very large because we don't know costs yet.
        dist = [100000000] * n
        #Tracks which points are already connected.
        Visit = [False] * n
        #how many connections added, total min cost
        edges, res = 0, 0
        #if there are n connections we need n-1 connections
        while edges < n - 1:
            #Marking the node as visited
            Visit[node] = True
            # -1 means No next node has been chosen yet
            nextNode = -1
            #Loop through every point.
            for i in range(n):
                #Skip if node already visited
                if Visit[i]:
                    continue
                #Cal the curr dist
                currdist = abs(points[i][0] - points[node][0]) + abs(points[i][1]-points[node][1])
                #store the min distance
                dist[i] = min(dist[i], currdist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    #Update nextNode to the node with the smallest distance found so far.
                    nextNode = i
            #cheapest node adding to res
            res += dist[nextNode]
            #Move to next node
            node = nextNode
            #Increase edge count as 1 more connection got added
            edges += 1
        return res
#TC: O(n^2)
#SC: O(n)

        
        