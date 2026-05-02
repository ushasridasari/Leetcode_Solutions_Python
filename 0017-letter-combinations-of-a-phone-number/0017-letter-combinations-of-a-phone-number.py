class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Creates a list to store final results.
        res = [] 
        #Mapping digits to letters
        digitToChar = { 
        "2": "abc",
        "3": "def", 
        "4": "ghi", 
        "5": "jkl", 
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv", 
        "9": "wxyz", 
        }
        #Defines a recursive function to build combinations.
        def backtrack(i, curStr):
            #Checks if the current string length equals input digits length.
            if len(curStr) == len(digits):
                #Adds the completed combination to result.
                res.append(curStr)
                #Stops further recursion for this path.
                return
            #Loops through letters of the current digit.
            for c in digitToChar[digits[i]]:
                #Moves to next digit and adds chosen letter to string.
                backtrack(i + 1, curStr + c)
        #Checks if input is not empty.
        if digits:
            #Starts recursion from index 0 with empty string.
            backtrack(0, "")
        #Returns all generated combinations.
        return res

        