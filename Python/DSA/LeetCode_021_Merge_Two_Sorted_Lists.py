class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        # Connect the smaller node to the merged list
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach any remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
      
