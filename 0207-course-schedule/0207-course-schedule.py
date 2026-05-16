class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Creating a graph i.e, 0: [], 1: []
        preMap = {i: [] for i in range(numCourses)}
        #This adds prerequisite courses. After loop preMap = {0: [1],1: [0]}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()
        #Creates a DFS function to check whether a course can be completed safely.
        def dfs(crs):
            #Checks whether the course is already in the current DFS path.
            if crs in visiting:
                #Returns False because a cycle is found.
                return False
            #Checks whether the course has no prerequisites.
            if preMap[crs] == []:
                #Returns True because the course can be completed directly.
                return True
            
            #Marks the current course as being visited.
            visiting.add(crs)
            #Loops through all prerequisite courses of the current course.
            for pre in preMap[crs]:
                #Checks whether the prerequisite course can be completed.
                if not dfs(pre):
                    #Returns False if any prerequisite course creates a cycle.
                    return False
            #Removes the current course from the visiting set after DFS finishes.
            visiting.remove(crs)
            #Marks the course as already verified safe.
            preMap[crs] = []
            #Returns True because the current course can be completed safely.
            return True
        #Loops through all courses one by one.    
        for c in range(numCourses):
            #Checks whether the current course can be completed.
            if not dfs(c):
                #Returns False if any course contains a cycle.
                return False
        #Returns True if all courses can be completed successfully.
        return True

#TC: O(V + E)
#SC: O(V + E)
#Where V is the number of courses and E is the number of prerequisites.
