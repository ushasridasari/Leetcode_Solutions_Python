# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        #create a set to store references of the visited nodes
        seen = set()
        #start pointer at the head node.
        curr = head
        #loop until curr becomes none
        while curr:
            #check if current node was already visited.
            if curr in seen:
                return True
            #if not visited add the refrence to the set
            seen.add(curr)
            #move to the next node
            curr = curr.next
        return False'''
        #initialising two pointers at the head
        slow, fast = head, head
        #loops through both fast and fast.next becomes none
        while fast and fast.next:
            #move slow pointer one step forward
            slow = slow.next
            #move fast pointer two step forward
            fast = fast.next.next
            #check if both pointers meet
            if slow == fast:
                return True
        return False
        