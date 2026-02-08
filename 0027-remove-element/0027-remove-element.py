class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        n = len(nums)
        arr = []
        #looping through each index in nums
        for i in range(n):
            # value at index is not equals to 3
            if nums[i] != val:
                arr.append(nums[i])
                k += 1
        for i in range(len(arr)):
            nums[i] = arr[i]
        return k

