class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            #i.e, left side is sorted
            if nums[l] <= nums[m]:
                #if the target is greater than nums[m] or less than nums[l], target will be in the right half
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                #If the target is less than nums[m], or greater than nums[r], target will be in the left half 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1