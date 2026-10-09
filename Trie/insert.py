"""
Trie Insertion

Problem:
    Insert a lowercase English word into a Trie.

Approach:
    For each character:
        1. Calculate its index from 0 to 25.
        2. Create a child node if it does not exist.
        3. Move to that child node.
    Mark the final node as the end of the word.

Time Complexity:
    O(L), where L = length of the word.

Space Complexity:
    O(1) auxiliary space per insertion, excluding newly
    allocated Trie nodes. At most O(L) new nodes are created.
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEndOfWord = False

def insert(node, key): # root is passed as node
    for ch in key:
        idx = ord(ch) - ord('a')

        if not node.child[idx]:
            node.child[idx] = TrieNode()

        node = node.child[idx]

    node.isEndOfWord = True