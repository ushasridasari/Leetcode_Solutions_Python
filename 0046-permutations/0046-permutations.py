class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Creates a list to store all permutations
        self.res = []
        #Starts the recursive process from index 0
        self.backtrack(nums, 0)
        #After all permutations are generated, return them.
        return self.res
    #This function generates permutations by fixing numbers at each position.
    def backtrack(self, nums: List[int], idx: int):
        #If we have filled all positions, a permutation is complete.
        if idx == len(nums):
            #Add a copy of the current arrangement to the result.
            self.res.append(nums[:])
            #Stops the combinations.
            return
        #Try placing each remaining number at the current position.
        for i in range(idx, len(nums)):
            #Place the selected number at the current position.
            nums[idx], nums[i] = nums[i], nums[idx]
            #Move to the next position and repeat the process
            self.backtrack(nums, idx + 1)
            #Swap back to restore the original list.
            nums[idx], nums[i] = nums[i], nums[idx]

    # TC: O(n!*n)
    # SC: O(n)
            

        


        