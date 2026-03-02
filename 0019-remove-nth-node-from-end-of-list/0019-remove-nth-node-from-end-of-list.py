# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Step1: Finding the total length of the linked list
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        #Step2: Converting 
        removeIndex = N - n
        #Step3: if the head is the node to remove, return to second node
        if removeIndex == 0:
            return head.next
        #Step4: Visit each node just before the one we want to remove
        cur = head
        for i in range(N - 1):
            #checking whether we reached the node just before target
            if (i + 1) == removeIndex:
                #skip the target node
                cur.next = cur.next.next
                break
            cur = cur.next
        #Step5: Return the head
        return head