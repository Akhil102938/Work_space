from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Store the frequency of each fruit type
        count = {}
        left = 0
        max_len = 0

        for right, fruit in enumerate(fruits):
            # Add the current fruit to the window
            count[fruit] = count.get(fruit, 0) + 1

            # Shrink the window if more than 2 fruit types exist
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1

                # Remove fruit type when its frequency becomes zero
                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            # Update the maximum valid window length
            max_len = max(max_len, right - left + 1)

        return max_len
      
