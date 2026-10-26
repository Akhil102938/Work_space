class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create the binary tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

count = 0
stack = [root]  # Start DFS from the root

while stack:
    current = stack.pop()
    count += 1  # Count the current node

    # Add child nodes to the stack
    if current.left:
        stack.append(current.left)

    if current.right:
        stack.append(current.right)

print(count)
