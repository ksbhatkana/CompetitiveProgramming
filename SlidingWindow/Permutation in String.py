from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # If s1 is longer than s2, no valid permutation can exist
            return False
        
        s1_count = Counter(s1)  # Frequency map of s1
        window_count = Counter()  # Frequency map of the current window in s2
        left = 0

        for right in range(len(s2)):
            # Add the current character to the window
            window_count[s2[right]] += 1

            # If the window is larger than s1, shrink from the left
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1      # The window slides forward, ensuring that each substring we check has exactly len(s1) characters.
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]  # Remove the key if count reaches 0
                left += 1

            # Compare window with s1_count
            if window_count == s1_count:          # works correctly because the window_count only ever contains exactly len(s1) characters at any time.

                return True  # Found a permutation

        return False  # No permutation found
