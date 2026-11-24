
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None
        curr = root
        stack = []

        # Perform iterative inorder traversal
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Detect incorrect order
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr

            prev = curr
            curr = curr.right

        # Restore the BST by swapping values
        if first and second:
            first.val, second.val = second.val, first.val
          
