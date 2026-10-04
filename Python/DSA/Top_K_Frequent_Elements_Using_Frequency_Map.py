class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Count frequency
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # Sort by frequency from highest to lowest
        sorted_freq = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # Return the first k elements
        return [item[0] for item in sorted_freq[:k]]
