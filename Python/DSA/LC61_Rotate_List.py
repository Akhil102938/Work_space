
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Handle empty list, single node, or zero rotation
        if not head or not head.next or k == 0:
            return head

        # Calculate the length and find the last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Remove unnecessary full rotations
        k %= length

        if k == 0:
            return head

        # Connect the tail to the head to form a circular list
        tail.next = head

        # Find the new tail position
        steps_to_new_head = length - k
        new_tail = head

        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        # Break the circle to get the rotated list
        new_head = new_tail.next
        new_tail.next = None

        return new_head
      
