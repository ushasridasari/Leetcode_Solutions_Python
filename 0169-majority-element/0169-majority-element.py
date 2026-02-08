class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #sorting all the numbers in an array
        nums.sort()
        #returning the middle element as it appears more that n/2 times
        return nums[len(nums) // 2]
                    
            


        