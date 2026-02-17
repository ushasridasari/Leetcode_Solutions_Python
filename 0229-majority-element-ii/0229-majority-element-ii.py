class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Storing the frequency of each number in a dictionary manner.
        count = Counter(nums)
        arr = []
        n = len(nums)
        #loops through each element in count
        for key in count:
            count[key]
            if  count[key] > n // 3:
                arr.append(key)
        return arr

# TC: O(n)
# SC: O(n)
        


            
        