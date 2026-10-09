"""
Maximum XOR Subarray

Problem:
    Find the maximum XOR value among all contiguous subarrays.

Approach:
    1. Use prefix XOR to represent subarray XORs.
    2. Store previous prefix XOR values in a binary Trie.
    3. Greedily choose the opposite bit at each position to
       maximize the XOR value.

Time Complexity:  O(32 * N) = O(N), for 32-bit integers.
Space Complexity: O(32 * N) = O(N), for the Trie.
"""

class TrieNode:
    def __init__(self):
        self.children = [None, None]


def maxSubarrayXOR(arr):
    root = TrieNode()

    def insert(num):
        node = root

        for bit in range(31, -1, -1):
            b = (num >> bit) & 1

            if node.children[b] is None:
                node.children[b] = TrieNode()

            node = node.children[b]

    def max_xor(num):
        node = root
        result = 0

        for bit in range(31, -1, -1):
            b = (num >> bit) & 1
            opposite = 1 - b

            if node.children[opposite] is not None:
                result |= (1 << bit)
                node = node.children[opposite]
            else:
                node = node.children[b]

        return result

        # Prefix XOR 0 allows subarrays starting at index 0.
    insert(0)

    prefix_xor = 0
    answer = 0

    for num in arr:
        prefix_xor ^= num

        answer = max(answer, max_xor(prefix_xor))
        insert(prefix_xor)

    return answer
