class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #EC: Empty s1?, s1 and s2 empty?, maxlength, s1 = s2, len(s1) > s2, if all chars same?
        #if s1 is longer then we couldn't able to find sub string
        if len(s1) > len(s2):
            return False
        #used to count the frequencies of the individual ele
        s1Count, s2Count = [0] * 26, [0] * 26
        #counting the characters in s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        #cal the number of characters whose frequency is equal in both arrays.
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        #slide the window by moving the right pointer across s2.
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            #convert the new right character into its 0–25 index.
            index = ord(s2[r]) - ord('a')
            #add the new right character to the window count.
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                #increase matches if frequencies becomes equal.
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                #decrease matches if adding the character broke a previous match.
                matches -= 1
            #convert the left character (to be removed) into its index
            index = ord(s2[l]) - ord('a')
            #remove the left character from the window count.
            s2Count[index] -= 1
            #increase matches if removing fixed a mismatch.
            if s1Count[index] == s2Count[index]:
                matches += 1
            #decrease matches if removing broke a previous match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            #move the left pointer to slide the window
            l += 1
        #returns true if final window has all matching frequencies
        return matches == 26

#TC: O(n)
#SC: O(1)
        
        