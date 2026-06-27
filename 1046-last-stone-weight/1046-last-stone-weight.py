class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Python heap only removes the smallest number first, But in the game we need the largest stone first. So we convert numbers to negative.
        stones = [-s for s in stones]
        #This arranges the list into a heap so we can quickly remove the largest stones.
        heapq.heapify(stones)
        #keep smashing stones until only one or zero stones remain
        while len(stones) > 1:
            #Removes the largest stone
            first = heapq.heappop(stones)
            #Removes the second largest stone
            second = heapq.heappop(stones)
            #checks if the stones have different weights
            if second > first:
                #insert the remaining stone weight.
                heapq.heappush(stones, first - second)
        #If both stones were equal, so we add 0
        stones.append(0)
    #Since we stored negative numbers, we convert back to positive using abs() i.e,abs(-1) = 1
        return abs(stones[0])