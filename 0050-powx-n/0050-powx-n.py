class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        res = 1
        for i in range(abs(n)):
            if n >= 0:
                res *= x
            else:
                res *= 1/x
        return res '''

        # if x is 0 then 0^n is 0
        if x == 0:
            return 0
        #if n is 0 then x^0 is 1
        if n == 0:
            return 1

        res = 1
        #Stores the postive value of n
        power = abs(n)
        #Runs the loop until power becomes 0
        while power:
            #checking whether the power is even or odd (if odd then False, even then true)
            if power & 1:
                #If power is odd, multiply current x into the answer.
                res *= x
            #We square x to create bigger powers.
            x *= x
            #It divides power by 2
            power = power // 2

        return res if n >= 0 else 1/res

#Tc: O(nlogn)
#SC: O(1)

        