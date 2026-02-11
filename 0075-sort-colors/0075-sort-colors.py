class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Creates a list with len 3 to store count of 0s, 1s and 2s
        count = [0] * 3
        #Loops through every number in nums
        for num in nums:
            #Incrementing the Count of the particular element
            count[num] += 1

        index = 0
        #Loops through the 0, 1, 2
        for i in range(3):
            #Repeats while there are remaining occurrences of value i
            while count[i]:
                #Decreasing the count of value of that elememt after placing
                count[i] -= 1
                #Places value i at the current position in nums
                nums[index] = i
                #Moving to next index
                index += 1
        