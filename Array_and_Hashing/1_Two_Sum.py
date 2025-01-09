class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
<<<<<<< HEAD
        
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

        
=======
       dict1 = defaultdict()
       for i, n in enumerate(nums):
            x = target - n
            if x in dict1:
                return [dict1[x], i]
            dict1[n] = i
>>>>>>> a88f4fad8abe162dbefbca42d005bf34f4f959ae
