class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #create an empty set to track numbers seen an odd number of times
        seen = set()
        for num in nums:
            # if this number was already seen before
            if num in seen:
                #removing the seen no. from the set
                seen.remove(num)
            else:
                #Adding into the set
                seen.add(num)
        #convert the set to a list and return its only remaining element
        return list(seen)[0]

#TC: O(n)
#SC: O()