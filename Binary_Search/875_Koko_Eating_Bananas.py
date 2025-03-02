class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #l = 1 i.e, koko can eat atleast 1 banana in an hour
        #r = max possibility of bananas that a koko can eat in an hour
        l, r = 1, max(piles)

        res = r
        while l <= r:
            #finding the mid value to know the middle eating speed
            k = (l + r) // 2
            #Calculating total time needed for koko
            total_time = 0
            for i in piles:
                total_time += math.ceil(float(i) / k)
            #if koko finishes in time
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
