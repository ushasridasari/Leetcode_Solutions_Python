
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def reverse(self, head):
    result = None
    # TODO: Write your code here
    prev = None
    curr = head

    while curr is not None:
      nextnode = curr.next
      if nextnode == None:
        result = curr
      curr.next = prev
      prev = curr
      curr = nextnode
    return result

