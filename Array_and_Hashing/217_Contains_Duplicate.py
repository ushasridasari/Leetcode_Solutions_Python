class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set() 
        myset.update(nums)
        if len(myset) != len(nums):
            return True
        return False
    

# Solution2

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for i in range(len(nums)):
            if nums[i] in myset:
                return True
            myset.add(nums[i])
        return False