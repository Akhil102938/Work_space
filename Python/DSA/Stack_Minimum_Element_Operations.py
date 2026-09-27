stack = []


def push():
    push_num = int(input("Enter push no. : "))
    stack.append(push_num)


def remove():
    if stack:
        stack.pop()
    else:
        print("Stack is empty!")


def min_element():
    if not stack:
        print("Stack is empty!")
        return

    sm = stack[0]

    # Find minimum element in stack
    for i in range(len(stack)):
        if stack[i] < sm:
            sm = stack[i]

    print("Min. no. in stack :", sm)


while True:
    print("\n1) Add a number in stack")
    print("2) Remove number")
    print("3) Print stack")
    print("4) Min. no. in stack")
    print("5) Break")

    option = int(input("Enter your choice: "))

    if option == 1:
        push()
    elif option == 2:
        remove()
    elif option == 3:
        print(stack)
    elif option == 4:
        min_element()
    elif option == 5:
        break
    else:
        print("Invalid choice!")
