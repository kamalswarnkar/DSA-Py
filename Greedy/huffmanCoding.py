"""
Huffman Coding is a lossless data compression algorithm.

The idea is to assign variable-length codes to input characters
based on their frequencies:
    • More frequent characters get shorter codes.
    • Less frequent characters get longer codes.

The generated codes are Prefix Codes, meaning that the code
assigned to one character is not a prefix of the code assigned
to another character. This allows the encoded bitstream to be
decoded without ambiguity.

Algorithm:
1. Create a leaf node for every character and insert all nodes
   into a Min Heap based on frequency.
2. While the heap contains more than one node:
       a. Extract the two nodes with minimum frequency.
       b. Create a new internal node whose frequency is the sum
          of the two nodes.
       c. Make the two extracted nodes its left and right children.
       d. Insert the new node back into the heap.
3. The remaining node is the root of the Huffman Tree.
4. Traverse the tree:
       • Left edge  → 0
       • Right edge → 1
5. The root-to-leaf path gives the Huffman code of each character.

Time Complexity:
    O(N log N)

Space Complexity:
    O(N)

where,
N = number of distinct characters

Note:
• Every input character is represented by a leaf node.
• Internal nodes do not represent actual input characters.
• The Huffman tree is built using a greedy strategy.
"""

import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq # freq of symbol
        self.symbol = symbol # symbol name (character)
        self.left = left # left node of curr node
        self.right = right # right node of curr node

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def huffmanCode(chars, freq):
    if not chars and not freq:
        return None
    
    n = len(chars)
    heap = []

    for x in range(n):
        heapq.heappush(heap, Node(freq[x], chars[x]))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Internal Nodes
        new_node = Node(
            left.freq + right.freq, 
            None, 
            left, 
            right
        )

        heapq.heappush(heap, new_node)

    return heap[0] if heap else None

def printCodes(root, code = ''): # root = heap[0]
    if not root:
        return
    
    if not root.left and not root.right: # complete huffman code found
        print(f"{root.symbol} -> {code}")
        return

    if root.left:
        printCodes(root.left, code + "0")
    if root.right:
        printCodes(root.right, code + "1")
