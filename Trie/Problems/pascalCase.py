"""
PascalCase Pattern Matching

Problem:
    Return all words whose sequence of uppercase characters
    starts with the given pattern.

Approach:
    Build a Trie using only uppercase characters from each word.
    Store matching words at each Trie node so that traversing
    the pattern leads directly to all matching words.

Time Complexity:  O(S + P + K), where:
                  S = total length of all input words,
                  P = length of the pattern,
                  K = number of matching words returned.
Space Complexity: O(S * U) in the worst case, where U is the
                  number of uppercase characters per word,
                  due to storing word references at each prefix.
"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.words = []

def pascalCase(arr, pat):
    root = TrieNode()

    def insert(word):
        node = root

        for ch in word:
            if ch.isupper():
                if ch not in node.child:
                    node.child[ch] = TrieNode()

                node = node.child[ch]
                node.words.append(word)

    for word in arr:
        insert(word)

    node = root

    for ch in pat:
        if ch not in node.child:
            return []

        node = node.child[ch]

    return node.words