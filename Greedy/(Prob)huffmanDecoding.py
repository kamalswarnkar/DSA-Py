"""
Huffman Decoding

Problem:
    Given a Huffman tree and an encoded binary string, decode the
    binary string and return the original text.

    Each leaf node contains a character, while internal nodes
    represent the combined Huffman tree structure.

Decoding Strategy:
1. Start traversal from the root.
2. For every bit in the encoded string:
       • 0 → move to the left child.
       • 1 → move to the right child.
3. Whenever a leaf node is reached:
       • Add its character to the result.
       • Restart traversal from the root.
4. Return the decoded string.

Time Complexity:
    O(L)

Space Complexity:
    O(L)

where,
L = length of the encoded binary string

Note:
• 0 represents a left edge.
• 1 represents a right edge.
• Every leaf node represents one character.
• After reaching a leaf, traversal restarts from the root.
• For a single-character Huffman tree, the character is repeated
  for every encoded bit.
"""

def huffmanDecode(root, binaryString):
    if not root:
        return ""
    
    if not root.left and not root.right:
        return root.data * len(binaryString)

    res = []
    curr = root

    for bit in binaryString:
        if bit == "0":
            curr = curr.left
        else:
            curr = curr.right

        if not curr.left and not curr.right:
            res.append(curr.data)
            curr = root

    return "".join(res)