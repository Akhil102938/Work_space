def removeDuplicates(s):
    stack = []

    for ch in s:
        # Remove adjacent duplicate
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


s = "abbaca"

print(removeDuplicates(s))
