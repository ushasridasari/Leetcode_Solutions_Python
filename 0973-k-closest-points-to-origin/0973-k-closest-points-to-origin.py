class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Creating an empty heap
        minHeap = []
        #Loop through x,y points
        for x, y in points:
            #Cal distance
            dist = x**2 + y**2
            #Adding it to minheap along with its x and y points
            minHeap.append([dist, x, y])
        #The smallest distance will come first
        heapq.heapify(minHeap)
        #creates a list to store res
        res = []
        #loops continues k times
        while k > 0:
            #removes the smallest distance from the heap.
            dist, x, y = heapq.heappop(minHeap)
            #Add That Point to Result
            res.append([x,y])
            #decrease the value of K
            k -= 1
        return res

    #TC: O(n + klogn)
    #SC: O(n)


        
        