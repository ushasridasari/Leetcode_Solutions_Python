class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            #i +=1
        return -1'''
        l, h = 0, len(nums) - 1
        while l <= h:
            #cal mid val
            mid = (l + h) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                h = mid - 1
            else:
                l = mid + 1
        return -1