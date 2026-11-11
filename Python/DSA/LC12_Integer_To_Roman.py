class Solution:
    def intToRoman(self, num: int) -> str:
        # Roman numeral values in descending order
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        # Corresponding Roman numeral symbols
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L",
                   "XL", "X", "IX", "V", "IV", "I"]

        res = []

        # Check each value from largest to smallest
        for i in range(len(values)):

            # Use the current symbol while its value fits
            while num >= values[i]:
                num -= values[i]
                res.append(symbols[i])

        # Join all symbols into one string
        return "".join(res)
      
