class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, n in enumerate(nums):
            x = i+1
            for j in range(x, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
#Solution2 using dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        