class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def generation(stack, openN, closeN):
            if openN == closeN == n:
                #Converts the stack list into a string and appending it to the result list.
                result.append("".join(stack))
                return
                #If open brace is less than 3, we can add another '(' to the stack.
            if openN < n:
                stack.append('(')
                #calls generation function with one more open parenthesis (openN + 1)
                generation(stack, openN + 1, closeN)
                #Removes the last added '(' (backtracks) to explore other possibilities.
                stack.pop()
                #If the number of close brace is less than the number of open braces, we can add ')'
            if closeN < openN:
                stack.append(')')
                #Recursively calls generation with one more close parenthesis (closeN + 1).
                generation(stack, openN, closeN + 1)
                #backtracking
                stack.pop()
        generation(stack, 0, 0)
        return result