class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #if either input is literally "0", result is "0"
        if "0" in (num1, num2):
            return "0"
        #product of two numbers has at most len(num1)+len(num2) digits
        res = [0] * (len(num1) + len(num2))
        #reverse so index i = ones, tens, hundreds
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                #multiply the two digits
                digit = int(num1[i1]) * int(num2[i2])
                #place value: digit at position i1 contributes to i1+i2
                res[i1 + i2] += digit
                #carry the overflow (tens place) into the next higher digit
                res[i1 + i2 + 1] +=  res[i1 + i2] // 10
                #keep current position as a single digit (0-9)
                res[i1 + i2] %= 10
               
        #reverse back to normal order
        res, beg = res[::-1], 0
        # # skip leading zeros, but leave at least one digit
        while beg < len(res)-1 and res[beg] == 0:
            #move pointer forward past each leading zero
            beg += 1
        #convert remaining digits to strings
        res = map(str, res[beg:])
        #join into final result
        return "".join(res)


#TC: O(m*n)
#SC: O(m+n)
