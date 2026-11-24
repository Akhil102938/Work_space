class Solution:
    def isNumber(self, s: str) -> bool:
        # Track whether digits, decimal point, and exponent exist
        seen_digit = False
        seen_dot = False
        seen_exponent = False

        for i, char in enumerate(s):

            # Check for digits
            if char.isdigit():
                seen_digit = True

            # Signs are allowed at the beginning or after e
            elif char in "+-":
                if i > 0 and s[i - 1].lower() != "e":
                    return False

            # Handle scientific notation
            elif char.lower() == "e":
                if seen_exponent or not seen_digit:
                    return False

                seen_exponent = True
                seen_digit = False

            # Handle decimal point
            elif char == ".":
                if seen_dot or seen_exponent:
                    return False

                seen_dot = True

            # Reject all other characters
            else:
                return False

        # A valid number must contain digits after all checks
        return seen_digit
      
