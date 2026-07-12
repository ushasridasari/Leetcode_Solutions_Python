class Solution:
    def isHappy(self, n: int) -> bool:
        #Creates an empty set to keep track of numbers we've already seen.
        visit = set()

        #Keeps looping until the current number repeats.
        while n not in visit:
            #Stores the current number in the set.
            visit.add(n)
            #Replaces n with the sum of the squares of its digits
            n = self.sumOfSquares(n)
            #Checks if the number has become 1
            if n == 1:
                #Returns True because the number is happy.
                return True
        #Returns false because the numbers started repeating and will never reach 1.
        return False

    #Defines a helper function to calculate the sum of the squares of a number's digits.
    def sumOfSquares(self, n: int) -> int:
        #Creates a variable to store the total sum.
        output = 0

        #Loops until all digits of the number have been processed.
        while n:
            #Gets the last digit of the number.
            digit = n % 10
            #Squares the last digit.
            digit = digit ** 2
            #Adds the squared digit to the total sum.
            output += digit
            #Removes the last digit from the number.
            n = n // 10
        #Returns the final sum of the squared digits.
        return output
        
#TC: O(logn)
#SC: O(logn)