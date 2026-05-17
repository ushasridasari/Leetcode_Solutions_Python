class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #To store the final course in the list format
        output = []
        #creating a set for cycle detection
        cycle = set()
        #Stores courses already completed safely
        visit = set()

        #Creating a DFS function to check whether a course is safe
        def dfs(crs):
            #If crs exists in the current path then a cycle exists
            if crs in cycle:
                return False
            #If course already verified safe, No need to call dfs function again
            if crs in visit:
                return True
            #if crs not in any of set then try to add it into cycle
            cycle.add(crs)
            #Verifies whether a course has a cycle by checking every prerequisite.
            for pre in preMap[crs]:
                #If any prerequisite has cycle, Current course also becomes invalid
                if dfs(pre) == False:
                    return False
            #DFS finished for current course, Remove from current DFS path.
            cycle.remove(crs)
            #Add it to the Visit node to mark it as safe
            visit.add(crs)
            #Course is added AFTER prerequisites finish
            output.append(crs)
            #Means current course is safe.
            return True
        #Run DFS On Every Course
        for c in range(numCourses):
            #if a cycle exsists
            if dfs(c) == False:
                #return empty list
                return []
        #Returns valid course order.
        return output

#TC: O(V + E)
#SC: O(V + E)

#V = number of courses (vertices/nodes)
#E = number of prerequisites (edges)

        