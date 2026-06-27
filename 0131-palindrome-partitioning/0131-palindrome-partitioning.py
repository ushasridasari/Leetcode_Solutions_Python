class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #res to store the result and part to store the curr path
        res, part = [], []

        #
        def dfs(i):
            #If we reached end of string
            if i >= len(s):
                #Save current partition into result
                res.append(part.copy())
                #Stops this path
                return
            #Trying all substrings starting from index i
            for j in range(i, len(s)):
                #Check if substring s[i:j+1] is palindrome
                if self.isPalin(s, i, j):
                    #Add this piece to current path
                    part.append(s[i : j+1])
                    #Move to next part of string
                    dfs(j+1)
                    #Remove last added piece to try another option
                    part.pop()

        #Start from index 0
        dfs(0)
        #Returning all the partitions
        return res

    def isPalin(self, s, l, r):
        #Compare from both ends
        while l < r:
            #If the left and right letters don't match return false
            if s[l] != s[r]:
                return False
            #Move inward
            l, r = l+1, r-1
        #If all matched then it is a palindrome
        return True

#TC: O(n*2^n)
#SC: O(n) and O(n*2^n)