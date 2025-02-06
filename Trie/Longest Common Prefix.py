from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)  # Automatically creates TrieNode when missing
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            node = node.children[char]  # No need to check existence, defaultdict handles it
        node.is_end = True
    
    def longest_common_prefix(self) -> str:
        prefix = ""
        node = self.root
        
        while node and len(node.children) == 1 and not node.is_end:
            char = next(iter(node.children))  # Get the single child key
            prefix += char
            node = node.children[char]
        
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.longest_common_prefix()
