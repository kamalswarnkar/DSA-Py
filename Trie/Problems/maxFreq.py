"""
Maximum Frequency Word Using Trie

Problem:
    Find the most frequent word in a sentence.
    If multiple words have the same maximum frequency,
    return the one that occurs first in the sentence.

Approach:
    Insert each word into a Trie and increment its frequency
    at the terminal node. Update the answer only when a
    strictly higher frequency is found.

Time Complexity:  O(N + L), where N is the sentence length
                  and L is the total length of inserted words.
Space Complexity: O(L), for the Trie nodes.
"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.freq = 0
        self.isEndOfWord = False

def insert(root, word):
    node = root

    for ch in word:
        if ch not in node.child:
            node.child[ch] = TrieNode()

        node = node.child[ch]

    node.isEndOfWord = True
    node.freq += 1

    return node.freq

def maxFreq(sentence):
    root = TrieNode()
    max_freq = 0
    max_word = ""

    for word in sentence.split():
        freq = insert(root, word)

        if freq > max_freq:
            max_freq = freq
            max_word = word

    return f"{max_word} {max_freq}"