class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_paragraph = ''.join(c.lower() if c.isalnum() else ' ' for c in paragraph)
        words = normalized_paragraph.split()
        
        # Create a set of banned words
        banned_set = set(banned)
        
        # Count occurrences of each word, excluding banned words
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Return the most common word
        return word_counts.most_common(1)[0][0]
