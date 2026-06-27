class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #To store the valid paranthesis
        res = []
        #creates a list to build the curr paranthesis string step by step
        stack = []
        #function to try diff parantheses combinations
        def backtrack(openN, closeN):
            #Checks if we have used all parentheses pairs
            if openN == closeN == n:
                #Joins the stack into a string and saves it.
                res.append("".join(stack))
                #Stops this path because the combination is complete
                return
            #We can add "(" only if we haven't used all opening brackets yet.
            if openN < n:
                #adding "(" to th stack
                stack.append("(")
                #Call the function again after adding "("
                backtrack(openN+1, closeN)
                #Removes the last parenthesis so we can try another possibility.
                stack.pop()
            #We can add ")" only if there are more "("
            if closeN < openN:
                ##adding "(" to th stack
                stack.append(")")
                ##Call the function again after adding ")"
                backtrack(openN, closeN+1)
                #Removes the last parenthesis so we can try another possibility.
                stack.pop()
        backtrack(0, 0)
        return res

    # TC: O(4^n/n^1/2)
    # SC: O(n)