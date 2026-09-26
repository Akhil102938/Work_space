def isValid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for x in s:
        if x in pairs:
            if not stack or stack[-1] != pairs[x]:
                return False

            stack.pop()
        else:
            stack.append(x)

    return not stack


print(isValid("()[]{}"))  # True
print(isValid("([{}])"))  # True
print(isValid("(]"))      # False
print(isValid("([)]"))    # False
