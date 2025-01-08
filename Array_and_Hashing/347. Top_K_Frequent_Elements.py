class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
        max = []
        for key, value in dict1.items():
            heappush(max, (-value, key))
        res = []
        while k > 0:
            value, key = heappop(max)
            res.append(key)
            k -= 1
        return res



                
        
            

