class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            #Add 1 if the value is 1 else 0
            res +=1 if n & 1 else 0
            # shift right to bring the next bit into position
            n >>= 1
        return res

#TC: O(1)
#SC: O(1)
