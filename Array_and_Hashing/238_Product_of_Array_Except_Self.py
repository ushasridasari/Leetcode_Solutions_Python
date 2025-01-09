class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        # TC: O(n)
        # SC: O(1)
        
        
        #solution 2
        list1 = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    list1[i] *= nums[j]    
        return list1 

        #solution 3
        n = len(nums)
        pref = [0] * n
        suf = [0] * n
        pref[0] = suf[n - 1] = 1
        # [1, 1, 2, 6]
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        # [24, 12, 4, 1]
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]
        res = [0] * n
        for i in range(n):
            res[i] = pref[i] * suf[i]
        return res
        # TC: O(n)
        # SC: O(n) 