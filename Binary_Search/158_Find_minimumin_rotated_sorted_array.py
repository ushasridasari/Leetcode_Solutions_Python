class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''res = min(nums)
        return res'''
        #initialising the res value to 1st ele
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            #that means left side is sorted
            if nums[l] <= nums[m]:
                #moving to right side
                l = m + 1
            else:
                r = m - 1
        return res

                