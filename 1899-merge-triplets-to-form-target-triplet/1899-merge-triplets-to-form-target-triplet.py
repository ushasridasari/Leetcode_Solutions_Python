class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Creating and Initially assiging all variables to False to check 3 trage values
        x = y = z = False
        #Goes through each triplet where t[0] = [2,5,3]....
        for t in triplets:
            #Verify:t[0] == target[0] whether the first number matches the target's first number;      t[1], t[2] is less than their respective targets. if Ture -> x = X or True 
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            #y becomes True if a triplet has the second target value exactly, while the other two values are not greater than the target.
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            #z becomes True if a triplet has the third target value exactly, while the other two values are not greater than the target.
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            #if all are true, then we can build a triplet
            if x and y and z:
                return True
        return False

#TC: O(n)
#SC: O(1)
        