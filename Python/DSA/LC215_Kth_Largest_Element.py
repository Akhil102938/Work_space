import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Keep the first k elements in a min heap
        heap = nums[:k]
        heapq.heapify(heap)

        # Check the remaining elements
        for num in nums[k:]:

            # Replace the smallest heap element if a larger one is found
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        # The smallest element in this heap is the kth largest overall
        return heap[0]
      
