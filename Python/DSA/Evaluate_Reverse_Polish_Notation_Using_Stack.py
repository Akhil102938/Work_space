def evalRPN(tokens):
    stack = []

    for token in tokens:
        try:
            num = int(token)
            stack.append(num)

        except:
            s1 = stack.pop()   # first popped = top
            s2 = stack.pop()   # second popped

            if token == "+":
                result = s2 + s1

            elif token == "-":
                result = s2 - s1

            elif token == "*":
                result = s2 * s1

            elif token == "/":
                result = int(s2 / s1)

            stack.append(result)

    return stack[0]


tokens = ["2", "1", "+", "3", "*"]

print(evalRPN(tokens))
