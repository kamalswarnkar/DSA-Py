"""
Assign Short Codes in Stream of Words

Problem:
    Generate the shortest prefix of each first-time city that
    distinguishes it from previously processed cities.
    For repeated cities, return the full city name followed
    by its occurrence count.

Approach:
    Store prefix counts in Trie nodes. The first prefix whose
    count is 1 is the shortest unique prefix. Track full-word
    occurrences separately for repeated city names.

Time Complexity:  O(N * L), where N is the number of cities
                  and L is the maximum city-name length.
Space Complexity: O(S), where S is the total number of
                  characters across all city names.
"""

class TrieNode:
    def __init__(self):
        self.child = {}

def renameCities(cities):
    root = TrieNode()
    freq = {}
    res = []

    def insert(city):
        node = root

        for char in city:
            if char not in node.child:
                node.child[char] = TrieNode()

            node = node.child[char]

    def shortestPrefix(city):
        node = root
        prefix = ""

        for char in city:
            prefix += char

            if char not in node.child:
                return prefix

            node = node.child[char]

        return city

    for city in cities:
        freq[city] = freq.get(city, 0) + 1

        if freq[city] > 1:
            code = f"{city} {freq[city]}"
        else:
            code = shortestPrefix(city)

        res.append(code)
        insert(city)

    return res