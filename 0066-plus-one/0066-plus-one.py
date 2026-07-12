class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        #Loops through the digits from the last digit to the first digit
        for i in range(n-1, -1, -1):
            #Checks if the current digit is less than 9
            if digits[i] < 9:
                #Adds 1 to the current digit.
                digits[i] += 1
                #Returns the updated list because no carry is needed.
                return digits
            #Changes the current digit from 9 to 0 because 9 + 1 = 10, so a carry is needed.
            digits[i] = 0
        #Adds 1 at the beginning of the list when all digits were 9
        return [1] + digits

    #TC: O(n)
    #SC: O(n)
        