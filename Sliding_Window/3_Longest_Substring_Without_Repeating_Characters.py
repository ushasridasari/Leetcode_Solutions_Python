class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        myset = set()
        while r < len(s):
            #removing the elements from the set until a first duplicate is found 
            while s[r] in myset:
                myset.remove(s[l])
                l +=1
            #adding the elements into the set without duplicates
            myset.add(s[r])
            #Calculating the length of set
            i = r - l + 1
            #finding the max value of the length of a set
            res = max(res, i)
            r += 1
        return res

        

        # bacabcd
        # abcaefg
        # abcd