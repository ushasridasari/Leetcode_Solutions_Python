class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #This list will store all the subsets we find.
        res = []
        #This list stores the current subset we are building.
        subset = []
        #Defines a recursive function that explores subsets starting from index i.
        def dfs(i):
            #Checks if we have finished looking at all numbers in the list.
            if i >= len(nums):
                #Saves a copy of the current subset into the result list.
                res.append(subset.copy())
                #Stops the function and goes back to the previous recursive call.
                return
            #Adds the current number nums[i] to the subset.
            subset.append(nums[i])
            #Recursively explores subsets that include the current number.
            dfs(i + 1)
        #Removes the last number from the subset to undo the previous choice (backtracking).
            subset.pop()
            #Recursively explores subsets that exclude the current number.
            dfs(i+1)
        #Start from 0
        dfs(0)
        return res

    #TC: O(n*2^n)
    #SC: O(O(n) extra space.&& O(2^n)for the output list

        