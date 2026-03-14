class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        #This converts the list into a min-heap structure i.e, the small val will be the top
        #[4,8,5,2] -> [2,4,8,5]
        heapq.heapify(self.minHeap)
        #Checks if the heap has more than k elements
        while len(self.minHeap) > k:
            #Removes the smallest element from the heap to keep only the k largest elements.
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #Inserts the new value val into the min-heap.
        heapq.heappush(self.minHeap, val)
        #Checks if the heap size exceeds k after insertion.
        if len(self.minHeap) > self.k:
        #Removes the smallest element so the heap still contains only the k largest numbers.
            heapq.heappop(self.minHeap)
    #Returns the smallest element in the heap, which represents the kth largest number overall.
        return self.minHeap[0]

    # TC: O(m*logk)
    # SC: O(k)

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)