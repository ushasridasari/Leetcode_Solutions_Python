class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''nums.sort()
        n = len(nums)
        return nums[n-k]'''
        #finding the k largest number and take the last number from them
        return heapq.nlargest(k, nums)[-1]
    #TC: O(nlogk)
    #SC: O(k)