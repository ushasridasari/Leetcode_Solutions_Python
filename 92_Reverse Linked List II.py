# class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next


class Solution:
    def reverse(self, head, p, q):
      # Store the original head as the result.
      result = head

      # If the list is empty or only one position is selected, return it.
      if head is None or p == q:
        return result

      # Move to the first node at position p.
      previous = None
      current = head

      for _ in range(p - 1):
        previous = current
        current = current.next

      # Reverse the nodes from position p to position q.
      for _ in range(q - p):
        node_to_move = current.next

        # Remove node_to_move from its current position.
        current.next = node_to_move.next

        
        if previous is not None:
          # new node points to old front
          node_to_move.next = previous.next
          # update front pointer to new node
          previous.next = node_to_move
        else:
          ## new node points to old front
          node_to_move.next = result
          # If p is 1, update the head.
          result = node_to_move

      # Return the new head.
      return result

