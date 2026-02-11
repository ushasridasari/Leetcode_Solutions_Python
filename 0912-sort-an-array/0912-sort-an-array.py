class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #max len, min len
        #Merge two sorted halves of arr from L→M and M+1→R
        def merge(arr, L, M, R):
            #copying the left and right subarrays
            left, right = arr[L:M+1], arr[M+1:R+1]
            # i = main index, j = left index and k = right index
            i, j, k = L, 0, 0
            # Compare elements of the both subarrays
            while j < len(left) and k < len(right):
                # If left element is smaller or equal to right element
                if left[j] <= right[k]:
                    # Add left element into original array
                    arr[i] = left[j]
                    # Move left pointer forward
                    j += 1
                else:
                    # Add right element into original array
                    arr[i] = right[k]
                    # Move right pointer forward
                    k += 1
                # Move main array pointer forward
                i += 1
            # If left half  has remaining elements
            while j < len(left):
                # Copy remaining left element
                arr[i] = left[j]
                # Move left pointer
                j += 1
                # Move main pointer
                i += 1
            # If right half  has remaining elements
            while k < len(right):
                # Copy remaining right element
                arr[i] = right[k]
                # Move right pointer
                k += 1
                # Move main pointer
                i += 1
        #merge sort function
        def mergeSort(arr, l, r):
            if l >= r:
                return
            # Find middle index
            m = (l + r) // 2
            # Recursively sort left half
            mergeSort(arr, l , m)
            # Recursively sort right half
            mergeSort(arr, m + 1 , r)
             # Merge the two sorted halves
            merge(arr, l, m, r)
        #Start merge sort on full array
        mergeSort(nums, 0, len(nums) - 1)
        # Return the sorted array
        return nums
        
        

        
                    
                
            
        