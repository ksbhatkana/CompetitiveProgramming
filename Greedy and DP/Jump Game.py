# DP is useful when we need all possible paths (e.g., counting ways to reach the end).
# Here, we only care if reaching the last index is possible, making Greedy a perfect fit.

#The greedy approach dynamically updates the max reachable index as it iterates through the array.
# It terminates early if it becomes clear that the last index is reachable.

#DP has TC O(N^2) and SC O(N) where GP has TC O(N) and SC O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i>max_reach:
                return False
            max_reach = max(max_reach, i+jump)
            if max_reach >= len(nums)-1:
                return True
