text = "A man, a plan, a canal: Panama"

left = 0
right = len(text) - 1

while left < right:

    # Skip non-alphanumeric characters from left
    while left < right and not text[left].isalnum():
        left += 1

    # Skip non-alphanumeric characters from right
    while left < right and not text[right].isalnum():
        right -= 1

    # Compare both characters
    if text[left].lower() != text[right].lower():
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")
