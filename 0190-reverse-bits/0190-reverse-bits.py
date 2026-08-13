class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            #Gets the i-th bit from n.
            bit = (n >> i) & 1
            #Moving that bit to the opposite side i.e, Moves that bit to its reversed position in res.
            res |= (bit << (31 - i))
        return res

#TC: O(1)
#SC: O(1)
        
        