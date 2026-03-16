class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #This list will store all the subsets we find.
        res = []
        #Sorts the numbers so duplicate numbers are next to each other
        nums.sort()
        #Defines a recursive function to create subsets.
        def backtrack(i, subset):
            #Checks if we have finished looking at all numbers in the list.
            if i == len(nums):
                #Adds a copy of the current subset to the result list.
                res.append(subset[::])
                #Stops the function and goes back to the previous recursive call.
                return
            #Adds the current number nums[i] to the subset.
            subset.append(nums[i])
            #Moves to the next number while keeping the current number included.
            backtrack(i + 1, subset)
        #Removes the last number so we can explore the case where the number is not included
            subset.pop()
            #This skips duplicate numbers.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            #Now explore the case where the current number is not included.
            backtrack(i+1, subset)
        #Start from 0
        backtrack(0, [])
        return res

    #TC: O(2^n)
    #SC: O(n)
        