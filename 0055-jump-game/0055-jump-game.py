class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #last index that we want to reach
        goal = len(nums) - 1

        #traversing backward: start = last index, stop = -1, step = -1
        for i in range(len(nums) - 1, -1, -1):
            #current index + jump value can reach goal
            if i + nums[i] >= goal:
                #If current position can reach goal, make current position the new goal(keep moving the goal to the left).
                goal = i
        #if goal reached the start index the return true else false
        return True if goal == 0 else False

    #TC: O(n)
    #SC: O(n)