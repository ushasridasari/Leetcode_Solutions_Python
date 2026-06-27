class Solution:
    def jump(self, nums: List[int]) -> int:
        #Count how many jumps we have taken
        res = 0
        #Set the current jump range to start at index 0.
        l = r = 0
        #Keep jumping until we reach the last box.
        while r < len(nums) - 1:
            #Store the farthest place we can reach in the next jump.
            farthest = 0
            #Check every position inside the current jump range
            for i in range(l, r + 1):
                #Update the farthest position we can reach.
                farthest = max(farthest, i + nums[i])
            #Move left boundary to next window.
            l = r + 1
            #This is the furthest we can reach in one more jump.
            r = farthest
            #Count one jump
            res += 1
        return res

    #TC: O(n)
    #SC: O(1)
        