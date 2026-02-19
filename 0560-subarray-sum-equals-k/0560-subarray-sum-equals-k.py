#EC : Empty?, Negative Numbers?, single element?, zero?

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''#Initializing a variable to coun the subarrays
        res = 0
        #Calculating the lenghth of nums
        n = len(nums)
        #Loops through each index in nums
        for i in range(n):
            sum = 0
            #Loops through th
            for j in range(i, n):
                #Adding the current value to sum
                sum += nums[j]
                #if the sum equals to k
                if sum == k:
                    #Count value increases
                    res += 1
        return res

#TC: O(n^2)
#SC: O(1)'''
        #res ->to store the total number of valid subarrays, cursum ->to store the prefix sum
        res = curSum = 0
        #Creates a dictionary to store prefix sum frequencies
        prefixSums = { 0 : 1 }
        #Loops through each element in nums
        for num in nums:
            #Add current ele to the prefix sum
            curSum += num
        #Calculates the previous prefix sum needed so that the current subarray sum equals k
            diff = curSum - k
            # Count how many valid subarrays end here
            res += prefixSums.get(diff, 0)
            # Store current prefix sum.
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
        