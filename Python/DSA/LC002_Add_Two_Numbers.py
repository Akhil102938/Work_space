from typing import Optional

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Create a dummy node to simplify building the result list
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Continue while either list has digits or carry remains
        while l1 or l2 or carry:

            # Get current digits; use 0 if a list has ended
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add both digits and the carry
            total = v1 + v2 + carry

            # Calculate the carry for the next position
            carry = total // 10

            # Store the current digit in a new node
            curr.next = ListNode(total % 10)

            # Move to the newly created node
            curr = curr.next

            # Move to the next node if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the first actual node, skipping the dummy node
        return dummy.next
      
