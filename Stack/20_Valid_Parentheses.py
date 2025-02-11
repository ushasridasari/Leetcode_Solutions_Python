class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #Mapping every close bracket to the open bracket using Hashmap
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            #If c is a closing bracket
            if c in closeToOpen:
                 # Check if stack is not empty and the top of the stack matches the corres open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    #removing the matched opening bracket from stack
                    stack.pop()
                else:
                    return False
            else:
                # If c is an opening bracket, push it onto the stack
                stack.append(c)
        #If stack is empty,it returns True or else returns False
        return True if not stack else False