class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #EC: Max len?, empty?, 
        '''Count = []
        for i in range(len(temperatures)):
            days = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    days = j-i
                    break
            Count.append(days)
             
        return Count'''

        #creates an array with 0's
        res = [0]*len(temperatures)
        #initilazing a stack
        stack = []
        #loops through each temp with its index
        for i, temp in enumerate(temperatures):
            #current temperature is warmer than the temperature at the index on top of stack.
            while stack and temperatures[stack[-1]] < temp:
                #Remove the previous colder day index from the stack.
                prev_index = stack.pop()
                #calculating the number of days
                res[prev_index] = i - prev_index 
            #Push current index into stack
            stack.append(i) 
        return res