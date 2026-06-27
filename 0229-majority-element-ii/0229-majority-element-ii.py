class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Storing the frequency of each number in a dictionary manner.
        count = Counter(nums)
        arr = []
        n = len(nums)
        #loops through each element in count
        for key in count:
            #If the number appears more than n/3 times
            if  count[key] > n // 3:
                #appending the key value to arr
                arr.append(key)
        return arr

# TC: O(n)
# SC: O(n)
        


            
        