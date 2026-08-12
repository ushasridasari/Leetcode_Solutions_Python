class Solution:
    def countBits(self, n: int) -> List[int]:
        #Creates a list containing n + 1 zeros to store the answer for every number from 0 to n.
        res = [0] * (n + 1)
        #Loops through every number from 0 to n.
        for i in range(n+1):
            #Finds how many 1s are in the binary form of i by using the answer we already calculated.
            #[i >> 1] Moves all binary bits of i one position to the right, which is basically the same as dividing by 2 and ignoring the decimal part.
            # (i & 1) Checks whether i is even or odd. if odd -> 1 if even -> 0
            res[i] = res[i >> 1] + (i & 1)
        return res  
        '''
        for i in range(n + 1):
            #Converts each digit to bits and cal ones
            digit = bin(i).count('1')
            res.append(digit)
        return res'''

#Tc: O(nlogn)
#SC: O(n)
        