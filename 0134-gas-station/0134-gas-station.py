class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Check if total gas is less than total travel cost
        if sum(gas) < sum(cost):
            #Return -1 because completing the circle is impossible.
            return -1
        #Store the current amount of gas in the tank.
        total = 0
        #Store the possible starting station
        res = 0
        #Visit each gas station one by one.
        for i in range(len(gas)):
            # Add gained gas and subtract travel cost.
            total += (gas[i] - cost[i])
            #Check if the gas tank becomes empty or negative.
            if total < 0:
                #Reset the gas tank because the current start failed.
                total = 0
                #Move the starting station to the next station.
                res = i + 1
        #Return the station index from which the whole trip is possible.
        return res

 #TC: O(n)
 #SC: O(1)
        