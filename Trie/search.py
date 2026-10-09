"""
Trie Search

Problem:
    Searches for a complete word in a Trie.

Approach:
    For each character:
        1. Calculate its index from 0 to 25.
        2. Return False if the child node does not exist.
        3. Move to that child node.
    Return whether the final node marks the end of a word.

Time Complexity:  O(L), where L is the length of the key.
Space Complexity: O(1) auxiliary space.
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEndOfWord = False

def search(node, key):
    for ch in key:
        idx = ord(ch) - ord('a')

        if not node.child[idx]:
            return False

        node = node.child[idx]

    return node.isEndOfWord