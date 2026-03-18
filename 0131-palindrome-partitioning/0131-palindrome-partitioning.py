class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Stores final answers
        res = []
        #Stores current values of the string
        path = []
        #Starts checking from index i
        def dfs(i):
            #If we reach end, Save current path and Stop
            if i >= len(s):
                res.append(path.copy())
                return
            #loop through each indeax of str
            for j in range(i, len(s)):
                #Only continue if substring is palindrome
                if self.isPalin(s, i, j):
                    #Add current part
                    path.append(s[i:j+1])
                    #Move to next path
                    dfs(j+1)
                    #Remove last part
                    path.pop()

        dfs(0)
        return res
    #Checks if substring is palindrome
    def isPalin(self, s, l, r):
        while l < r:
            #If letters don’t match then not palindrome
            if s[l] != s[r]:
                return False
            #Move inward
            l, r = l +1, r -1
        return True
    #TC: O(n*2^n)
    #SC: O(n*2^n)

        