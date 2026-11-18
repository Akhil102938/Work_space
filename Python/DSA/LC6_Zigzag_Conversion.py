class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an empty string for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        # Place characters in zigzag order
        for char in s:
            rows[curr_row] += char

            # Change direction at the top and bottom rows
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            curr_row += 1 if going_down else -1

        # Combine all rows to get the final string
        return ''.join(rows)
      
