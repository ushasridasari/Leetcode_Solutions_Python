class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Store the maximum subarray sum found so far.
        maxSub = nums[0]
        #Variable to store the current running subarray sum.
        curSum = 0

        #Loop through every number in the array.
        for n in nums:
            #Check if current sum became negative.(if negative prefix found)
            if curSum < 0:
                #Reset current sum.(Ignore the old subarray and start a new one)
                curSum = 0
            #Adding the current number to the running sum
            curSum += n
            #Comparing both sums to find the maximum sum
            maxSub = max(maxSub, curSum)
        #returning the largest subarray sum
        return maxSub

#TC: O(n)
#SC: O(1)

    


        