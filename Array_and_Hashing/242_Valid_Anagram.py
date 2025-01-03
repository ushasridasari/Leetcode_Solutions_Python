class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = defaultdict(list)
        dict2 = defaultdict(list)
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict2[t[i]] = dict2.get(t[i], 0) + 1
        if dict1 == dict2: # return dict1 == dict2 
            return True
        return False