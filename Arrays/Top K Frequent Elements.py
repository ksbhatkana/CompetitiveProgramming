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

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Time Complexity Analysis
# Operation	Complexity	Explanation
# Counting elements (Counter(nums))	O(N)	Scans nums once to compute frequencies.
# Building a heap of size k (heapq.nlargest())	O(N log k)	Uses a Min-Heap of size k, which is more efficient than full sorting.
# Total Complexity	O(N log k)	Faster than sorting (O(N log N)).

# Breaking it Down:
# First Argument (k) → The number of top elements to return.
# Second Argument (map_key.keys()) → The list of unique elements (keys from the frequency dictionary).
# Third Argument (map_key.get) → The function used to rank elements (based on frequency).
# map_key.get Determines Which Element is Considered as the Largest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_key = Counter(nums)
        return heapq.nlargest(k, map_key.keys(), map_key.get)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the occurrences of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Place numbers into the bucket based on their frequency
        for n, c in count.items():
            freq[c].append(n)

        # Collect the top K frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Iterate from highest frequency to lowest
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Best solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = defaultdict(list)

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums)+1, 0, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                return res[:k]
