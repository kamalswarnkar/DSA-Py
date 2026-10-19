# Data Structures and Algorithms in Python

> A structured, code-first collection of **262 Python implementations** covering core data structures, algorithmic techniques, and common problem patterns.

This repository is a personal learning archive built while completing the **[GeeksforGeeks Data Structures and Algorithms | DSA Course - Self Paced](https://www.geeksforgeeks.org/courses/dsa-self-paced)** course. It is intended for educational use: to revisit concepts, compare approaches, trace algorithms, and practise implementation in Python.

The code was written as part of that learning journey. It is not an official GeeksforGeeks repository, a production library, or a drop-in package.

## What this repository offers

- **Breadth across DSA fundamentals** - linear data structures, trees, graphs, hashing-adjacent tries, heaps, disjoint sets, and more.
- **Algorithmic problem-solving patterns** - recursion, backtracking, greedy algorithms, graph traversal, shortest paths, minimum spanning trees, and dynamic programming.
- **Approach comparisons** - many dynamic-programming problems are solved using recursion, memoization, tabulation, and, where useful, space optimization.
- **Focused, standalone examples** - each file concentrates on one concept or problem, making it easy to open, run, modify, and study in isolation.
- **Learning notes and visuals** - selected topics include Markdown explanations and diagrams, especially for trees, graphs, heaps, greedy algorithms, and range-query structures.

## Repository at a glance

| Item | Coverage |
| --- | --- |
| Language | Python |
| Python source files | 262 |
| Main subject areas | 11 |
| Supporting learning notes | Graphs, Trees, Heaps, Greedy Algorithms, Segment Trees, Binary Indexed Trees, and BST balancing |
| Diagram assets | 14 |
| External runtime dependencies | None required for the included examples |

## Topics and learning path

The folders follow a natural progression from foundational structures to advanced techniques. File names are deliberately descriptive, so they also work as a topic index.

| Area | Examples of concepts and problems included |
| --- | --- |
| [`Linked List`](./Linked%20List) | Singly, doubly, and circular linked lists; insertion, deletion, traversal, reversal, sorting, middle node, intersection, loop detection/removal, cloning, LRU cache, merging, palindrome checks, and pairwise swap |
| [`Stack`](./Stack) | List, deque, and linked-list stacks; two stacks, k stacks, minimum and frequency stacks, balanced parentheses, expression conversion/evaluation, stock span, next/previous greater or smaller elements, histogram/rectangle area, and celebrity problem |
| [`Queue`](./Queue) | List, linked-list, and circular queues; deque implementations and applications such as reversing a queue, number generation, circular tour, maximum subarray window, and designing a new data structure |
| [`Trees`](./Trees) | Binary-tree construction and traversals; height, size, diameter, views, LCA, width, serialization, subtree checks, tree conversion, maximum path/non-adjacent sums, burn tree, BST operations, AVL trees, segment trees, and binary indexed trees |
| [`Heap`](./Heap) | Heap implementation, `heapq`, heap sort, k-sorted arrays, running median, and merging k sorted collections |
| [`Trie`](./Trie) | Trie insertion, search, deletion, distinct rows, city renaming, Pascal-case generation, maximum XOR, and maximum-frequency strings |
| [`Graph`](./Graph) | Adjacency lists/matrices, BFS, DFS, connected components, cycle detection, articulation points, bridges, topological sorting, strongly connected components, shortest paths, and minimum spanning trees |
| [`Disjoint Set`](./Disjoint%20Set) | Find/union, union by rank, path compression, cycle detection, connected components, and Kruskal's algorithm |
| [`Greedy`](./Greedy) | Activity selection, fractional knapsack, job scheduling, Huffman coding/decoding, and largest-number construction |
| [`Backtracking`](./Backtracking) | Search trees, subsets, combinations, permutations, string search, expression generation, N-Queens, Sudoku, rat in a maze, graph coloring, knight attacks, and related problems |
| [`Dynamic Programming (DP)`](./Dynamic%20Programming%20%28DP%29) | Core DP patterns and 60+ implementations spanning knapsack, subset sum, coin change, LCS/LIS, edit distance, matrix-chain multiplication, palindrome partitioning, egg dropping, optimal game strategy, minimum jumps, and more |

## Deep-dive coverage

### Dynamic Programming

Dynamic programming is the largest section of the repository and emphasizes how one recurrence can be transformed into increasingly efficient solutions.

- **Foundational patterns:** recursion, memoization, tabulation, and 1D/space-optimized DP.
- **Selection and partition problems:** 0/1 knapsack, subset sum, coin change, minimum coins, rope cutting, and allocating minimum pages.
- **Sequence problems:** longest common subsequence (LCS), longest increasing subsequence (LIS), edit distance, and variations of LCS/LIS.
- **Optimization and interval-style problems:** matrix-chain multiplication, palindrome partitioning, egg dropping, count BSTs, and optimal strategy for a game.
- **Additional practice:** unique paths, minimum jumps, stair-counting variants, sum of substrings, and maximum sum with non-adjacent constraints.

For a representative comparison, the 0/1 Knapsack directory includes recursive, memoized, tabulated, and optimized-tabulation solutions. The optimized version illustrates the important right-to-left capacity update needed to prevent an item from being reused.

### Trees and range queries

The tree section moves from binary-tree basics to specialised structures and query techniques:

- DFS, BFS, spiral, and vertical traversals.
- Structural properties such as balance, foldability, identical/subtree checks, serialization, diameter, and maximum width.
- BST search-oriented operations, including floor, ceil, kth-smallest element, fixing a swapped BST, pair sum, and AVL rebalancing.
- Segment Tree and Binary Indexed Tree (Fenwick Tree) implementation, updates, prefix/range queries, and applied range-query problems.

### Graph algorithms

The graph section covers graph representation before progressing to standard traversal and optimization algorithms:

- Adjacency-list and adjacency-matrix representations.
- BFS and DFS, including disconnected graphs and path/counting problems.
- Directed and undirected cycle detection, bridges, articulation points, topological sorting, and strongly connected components (Kosaraju and Tarjan-style implementations).
- Shortest paths with BFS, DAG relaxation, Dijkstra's algorithm, and Bellman-Ford.
- Minimum spanning trees with Prim's and Kruskal's algorithms, with disjoint-set support available in the separate `Disjoint Set` section.

## How to use this repository

### Prerequisites

- Python 3
- No third-party packages are needed for the included scripts.

### Run an example

Clone the repository and run a file directly:

```bash
git clone https://github.com/kamalswarnkar/DSA-Py.git
cd DSA-Py
python "Graph/Shortest Path/shortestPath_III(Dijkstra).py"
```

Many files define a function or class rather than printing a full demonstration. In those cases, open the file, study the implementation and docstring, then add a small driver call or import the function into your own practice script.

For example, the following imports the optimized 0/1 Knapsack solution. Because some directories contain spaces and parentheses, `importlib` provides a convenient way to load a file by path:

```python
from importlib.util import module_from_spec, spec_from_file_location

path = "Dynamic Programming (DP)/0-1_Knapsack/optimized.py"
spec = spec_from_file_location("knapsack", path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

print(module.knapsack([60, 100, 120], [10, 20, 30], 50))  # 220
```

## Suggested study workflow

1. Start with the relevant Markdown notes where available, such as [`Graph/Intro.md`](./Graph/Intro.md), [`Trees/Intro.md`](./Trees/Intro.md), or [`Greedy/Intro.md`](./Greedy/Intro.md).
2. Read one focused implementation and identify its inputs, return value, and complexity note.
3. Trace the provided logic with a small example on paper or with `print` statements.
4. Reimplement it without looking, then compare the two versions.
5. For DP problems, study the recursion first, then memoization, tabulation, and the optimized solution to understand the trade-offs.
6. Change edge cases, input sizes, or data layouts to test your understanding.

## Code conventions and scope

- Implementations favor readability and learning over a uniform production API.
- Files are intentionally self-contained; class and function names may repeat across different directories.
- Inputs, sample data, output behavior, and indexing conventions are defined locally in each program.
- Time and space complexity notes are included in many source-file docstrings.
- Some file names retain the informal naming used during study (for example, `*_I`, `*_II`, and `(Prob)` markers); these are topic cues rather than versioned public APIs.

## Course acknowledgement

This repository was created while learning from GeeksforGeeks' paid **DSA with Python - Self Paced** course. The author has completed the course; the completion certificate is available [here](https://media.geeksforgeeks.org/courses/certificates/e4b72c057c5fb1e3ad35474d1264e5f0.pdf).

The repository is an independent set of personal implementations and study notes. Course names, trademarks, and learning material remain the property of their respective owners.

## Contributing

This is primarily a personal educational repository, but suggestions that improve correctness, clarity, examples, documentation, or complexity explanations are welcome.

If you contribute:

1. Keep each implementation focused on one concept or problem.
2. Add a concise docstring describing the problem, approach, complexity, and assumptions.
3. Prefer descriptive names and include a small demonstration when it improves discoverability.
4. Avoid introducing unnecessary external dependencies.

## License

No license file is currently included. Do not assume permission for reuse beyond viewing and learning from the code; contact the repository owner before redistributing or using it in another project.

---

If this repository helps your DSA practice, consider starring it and using it as a companion while you implement the same ideas yourself.
