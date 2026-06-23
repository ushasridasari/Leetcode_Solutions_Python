class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        #Loops through each character in the string
        for c in s:
            #Checks if the current character is an opening parenthesis.
            if c == '(':
                #Both minimum and maximum unmatched opening brackets increase by 1.
                leftMin, leftMax = leftMin + 1, leftMax + 1
            #Checks if the current character is a closing parenthesis.
            elif c == ')':
                #Both minimum and maximum unmatched opening brackets decrease by 1
                leftMin, leftMax = leftMin - 1, leftMax - 1
            #Handles the '*' character
            else:
                #'*' can act as ')', '(', or empty, so the range of possible unmatched brackets expands.
                leftMin, leftMax = leftMin - 1, leftMax + 1
            #Checks if even the maximum possible opening brackets become negative. ex: ())) or ))((
            if leftMax < 0:
                #Returns False because there are too many closing brackets.
                return False
            #Checks if the minimum possible opening brackets became negative.
            if leftMin < 0:
                #Resets leftMin to 0 since unmatched opening brackets cannot be less than zero.
                leftMin = 0
        #Returns True only if it is possible to end with zero unmatched opening brackets.
        return leftMin == 0

#TC: O(n)
#SC: O(1)
        