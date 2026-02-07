class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        #arr len equals to 2 times of nums len
        for i in range(2) :
            #appending each element from nums
            for num in nums:
                arr.append(num)
        return arr
        