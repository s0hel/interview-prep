# 703. Kth Largest Element in a Stream
# Solved
# Easy
# Topics
# Companies
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
#
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
#
#
# Example 1:
#
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
#
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = [0]

        for n in nums:
            self.push_heap(n)

    def push_heap(self, val: int):
        if len(self.heap) == 1:
            self.heap.append(val)
            return
        self.heap.append(val)
        idx = len(self.heap) - 1

        while idx > 1 and self.heap[idx // 2] > self.heap[idx]:
            # swap parent and child
            self.heap[idx // 2], self.heap[idx] = self.heap[idx], self.heap[idx // 2]
            idx = idx // 2

    def pop_heap(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        last_idx = len(self.heap) - 1
        last_val = self.heap[last_idx]
        self.heap[1] = last_val
        # or self.heap[1] = self.heap.pop()
        idx = 1

        while 2 * idx < len(self.heap):
            # if both children exist, compare with right child first
            if (2 * idx + 1 < len(self.heap)
                    and self.heap[2 * idx + 1] < self.heap[2 * idx]
                    and self.heap[2 * idx + 1] < self.heap[idx]):
                self.heap[idx], self.heap[2 * idx + 1] = self.heap[2 * idx + 1], self.heap[idx]
                idx = 2 * idx + 1
            elif self.heap[2 * idx] < self.heap[idx]:
                self.heap[idx], self.heap[2 * idx] = self.heap[2 * idx], self.heap[idx]
                idx = 2 * idx
            else:
                break

        return res

    class KthLargest:

        def __init__(self, k: int, nums: List[int]):
            self.minHeap, self.k = nums, k
            heapq.heapify(self.minHeap)
            while len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

        def add(self, val: int) -> int:
            heapq.heappush(self.minHeap, val)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
            return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
