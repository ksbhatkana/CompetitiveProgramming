# Time Complexity: 𝑂(𝑁×𝑀) in worst case
# Space Complexity: O(N×M) in worst case
# DFS naturally follows a recursive "spread-out" pattern that mimics how the fill propagates in an image. A recursive function is easy to implement and closely resembles how a color change would "spread" in connected pixels. It eliminates the need for a queue management system (which BFS requires).
# If the flood fill region is very large (e.g., filling an entire 1000 × 1000 grid), DFS can cause stack overflow due to deep recursion. BFS avoids this issue because it uses an explicit queue instead of recursion.

def flood_fill_dfs(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:  # If already colored, return early
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return
        
        image[r][c] = newColor  # Change color
        # Recursively fill in all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    dfs(sr, sc)
    return image

# Example Usage
image = [
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 1]
]
sr, sc, newColor = 1, 1, 2  # Start at (1,1) and replace with color 2
result = flood_fill_dfs(image, sr, sc, newColor)

# Print Result
for row in result:
    print(row)
