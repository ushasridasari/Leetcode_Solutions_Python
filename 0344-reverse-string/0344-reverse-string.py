class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #EC: empty?, singleele?.
        n = len(s)
        #Initializes a pointer at the beginning of the list
        left = 0
        #Initializes a pointer at the end of the list.
        right = n - 1
        #swapping until both pointers meet i.e, at mid value.
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        


        
        
        
            

        