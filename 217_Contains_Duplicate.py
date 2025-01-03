class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set() 
        myset.update(nums)
        if len(myset) != len(nums):
            return True
        return False