class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = 0
        max_freq = max_length = 0

        for right in range(len(s)):
            count[s[right]] +=1
            max_freq = max(max_freq, count[s[right]])
            while (right-left+1) - max_freq > k:
                count[s[left]] -=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length
