class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        n = len(nums)
        arr = []
        #looping through each index in nums
        for i in range(n):
            # value at index is not equals to 3
            if nums[i] != val:
                #adding the value to array
                arr.append(nums[i])
                #increasing the len of the arr
                k += 1
        #copying all the elements to nums as we need to return nums len
        for i in range(len(arr)):
            nums[i] = arr[i]
        return k

