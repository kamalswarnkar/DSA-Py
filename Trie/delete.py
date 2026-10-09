"""
Trie Deletion

Problem:
    Deletes a word from a Trie without affecting other words
    that share its prefix.

Approach:
    1. Traverse recursively to the end of the key.
    2. Unmark the terminal node.
    3. Delete nodes that have no children and are not the
       end of another word.
    4. Preserve shared-prefix nodes.

Time Complexity:  O(L), where L is the length of the key.
Space Complexity: O(L), due to recursive call stack.
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEndOfWord = False

def isEmpty(root): # A node is empty if it has no children.
    for x in root.child:
        if x != None:
            return False

    return True

def delNode(node, key, i = 0):
    if node is None:
        return None

    if i == len(key): # Unmark the word without affecting longer words.
        if node.isEndOfWord:
            node.isEndOfWord = False
    else:
        idx = ord(key[i]) - ord('a')
        node.child[idx] = delNode(node.child[idx], key, i + 1) # Delete recursively and update the child reference.

    if isEmpty(node) and not node.isEndOfWord:
        node = None

    return node