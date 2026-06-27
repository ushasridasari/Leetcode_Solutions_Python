class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Creates an empty dictionary to store the last position of each character.
        lastIndex = {}
        #Creating a hashmap to assign each char to its last index
        for i, c in enumerate(s):
            lastIndex[c] = i

        #Creates an empty list to store the partition sizes.
        res = []
        #Initializes the current partition size and partition end index to 0.
        size = end = 0
        #Loops through the string again to find valid partitions
        for i, c in enumerate(s):
            #Increases the size of the current partition by 1.
            size +=1
            #Updates the partition's ending position to the farthest last occurrence of any character seen so far.
            end = max(end, lastIndex[c])

            #Checks if the current index has reached the end of the partition.
            if i == end:
                #Adds the completed partition size to the result list.
                res.append(size)
                #Resets the partition size for the next partition.
                size = 0
        #Returns the list of partition sizes.
        return res

#TC: O(n)
#SC: O(m)