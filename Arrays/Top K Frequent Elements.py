# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Time Complexity Analysis
# Operation	Complexity	Explanation
# Counting elements (Counter(nums))	O(N)	Scans nums once to compute frequencies.
# Building a heap of size k (heapq.nlargest())	O(N log k)	Uses a Min-Heap of size k, which is more efficient than full sorting.
# Total Complexity	O(N log k)	Faster than sorting (O(N log N)).

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_key = Counter(nums)
        return heapq.nlargest(k, map_key.keys(), map_key.get)
