class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Stores all valid combinations
        res = []
        #sorting the numbers,so we can stop early when the sum exceeds target.
        candidates.sort()
        #Creates a helper function to try different number combinations.
        def dfs(i, curr, total):
            #If the sum becomes equal to target
            if total == target:
                #Save the combination
                res.append(curr.copy())
                #Stops exploring this path because we already found a valid combination.
                return
            #Loops through the numbers starting from index i
            for j in range(i, len(candidates)):
                #Checks if the current number is a duplicate of the previous number..
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                #Checks if adding this number makes the sum larger than the target.
                if total + candidates[j] > target:
                    break
                #Adds the current number to the combination.
                curr.append(candidates[j])
                #Recursively tries to build more combinations using the same number again.
                dfs(j+1, curr, total + candidates[j])
                #Removes the last number so we can try a different number (backtracking).
                curr.pop()
        #Starts the search with an empty combination and sum = 0.
        dfs(0, [], 0)
        return res

    #TC: O(n*2^n)
    #SC: O(n)
        