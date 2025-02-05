class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Pad the shorter version with zeros
        length = max(len(v1), len(v2))
        v1.extend([0] * (length - len(v1)))
        v2.extend([0] * (length - len(v2)))
        
        for i in range(length):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        
        return 0

# Test cases
solution = Solution()
print(solution.compareVersion("1.2", "1.10"))   # Output: -1
print(solution.compareVersion("1.01", "1.001")) # Output: 0
print(solution.compareVersion("1.0", "1.0.0"))  # Output: 0
