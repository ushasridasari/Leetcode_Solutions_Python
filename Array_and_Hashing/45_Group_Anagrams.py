class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        res = defaultdict(list)
        for s in strs:
<<<<<<< HEAD
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
=======
            sortS = ''.join(sorted(s))
            res[sortS].append(s)
>>>>>>> a88f4fad8abe162dbefbca42d005bf34f4f959ae
        return list(res.values())