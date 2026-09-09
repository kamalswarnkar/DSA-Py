# Greedy Algorithms --- Notes

## 1. What is a Greedy Algorithm?

**Greedy** is an algorithmic paradigm that builds a solution **piece by
piece**, always choosing the next piece that offers the most obvious and
immediate benefit.

The central idea is:

> **Make the best-looking choice right now, without worrying about
> changing that choice later.**

A greedy approach is a good fit when a sequence of **locally optimal
choices** leads to the **globally optimal solution**.

### Key idea

At every step:

1.  Look at the remaining choices.
2.  Pick the choice that looks best **right now**.
3.  Check whether that choice is feasible.
4.  If it is feasible, add it to the solution.
5.  Continue until all relevant items have been considered.

------------------------------------------------------------------------

## 2. General Structure of a Greedy Algorithm

A generic greedy algorithm can be represented as:

``` python
def getOptimal(arr):
    res = 0

    while (all items are not considered):
        i = selectItem()

        if feasible(i):
            res = res + i

    return res
```

### What each part means

-   `res = 0`\
    Initialize the solution.

-   `selectItem()`\
    Choose the next item according to the **greedy criterion** --- the
    choice that appears most beneficial at the current step.

-   `feasible(i)`\
    Check whether selecting the item keeps the partial solution valid.

-   `res = res + i`\
    If the choice is valid, permanently add it to the solution.

### Important characteristic

Once a greedy choice is made, it is generally **not reconsidered**.

That is what makes greedy algorithms attractive: they are often simple
and efficient.

------------------------------------------------------------------------

# 3. When Can Greedy Be Used?

A greedy algorithm can be applied when:

> **At every step, we can make a choice that looks best at the moment,
> and that choice still allows us to obtain an optimal solution for the
> complete problem.**

In other words:

**Local optimum → Global optimum**

But this is **not true for every optimization problem**.

A greedy strategy may produce a valid solution that is **not optimal**.

So whenever using greedy, the important question is:

> **Why is the locally best choice guaranteed not to hurt the final
> answer?**

This is the part that usually needs a proof or a convincing argument.

------------------------------------------------------------------------

# 4. Example: Fractional Knapsack

## Problem

Given a list of items, where every item has:

-   a **value**
-   a **weight**

and a knapsack with capacity `W`, fill the knapsack so that its total
value is **maximum possible**.

### Important condition

> **Fractions of an item are allowed.**

This condition is what makes the greedy strategy work.

------------------------------------------------------------------------

## Greedy Choice

For every item, calculate:

\[ `\text{value-to-weight ratio}`{=tex} =
`\frac{\text{value}}{\text{weight}}`{=tex} \]

Then:

> **Always choose the available item with the maximum value/weight
> ratio.**

If the entire item does not fit, take only the fraction that fits.

### Why does this work?

Suppose one item gives more value per unit of weight than another.

If we have some remaining capacity, using that capacity on the item with
the higher ratio always gives us more value.

Because **fractions are allowed**, we can keep taking the best ratio
item until the knapsack is full.

Therefore, the local greedy choice leads to the global optimum.

### Core takeaway

**Fractional Knapsack → sort/select by highest `value / weight` ratio.**

------------------------------------------------------------------------

# 5. Example: Activity Selection Problem

## Problem

You are given `N` activities with their **start** and **finish** times.

A person can perform only **one activity at a time**.

The goal is:

> **Select the maximum possible number of non-overlapping activities.**

------------------------------------------------------------------------

## Example 1

Activities are already sorted by finish time:

``` text
start[]  = {10, 12, 20}
finish[] = {20, 25, 30}
```

The maximum number of activities is **2**.

One optimal selection is:

``` text
{0, 2}
```

That means:

-   Activity `0`: `[10, 20]`
-   Activity `2`: `[20, 30]`

Activity `2` can start exactly when activity `0` finishes.

So the compatibility condition is:

``` text
start[i] >= finish[previous]
```

------------------------------------------------------------------------

## Example 2

Six activities, sorted by finish time:

``` text
start[]  = {1, 3, 0, 5, 8, 5}
finish[] = {2, 4, 6, 7, 9, 9}
```

The maximum number of activities is **4**.

One optimal set is:

``` text
{0, 1, 3, 4}
```

The selected activities are:

``` text
Activity 0: [1, 2]
Activity 1: [3, 4]
Activity 3: [5, 7]
Activity 4: [8, 9]
```

Each activity starts after or exactly when the previous selected
activity finishes.

------------------------------------------------------------------------

# 6. Greedy Strategy for Activity Selection

The greedy choice is:

> **Always select the next activity whose finish time is the smallest
> among the remaining compatible activities.**

This means we want to finish the current activity as early as possible,
leaving the largest possible amount of time for future activities.

## Algorithm

### Step 1 --- Sort

Sort all activities according to their **finish time** in ascending
order.

### Step 2 --- Select the first activity

Choose the first activity because it has the earliest finish time.

### Step 3 --- Scan the remaining activities

For every remaining activity:

-   If

``` text
start[i] >= finish[previously selected activity]
```

then select it.

-   Otherwise, skip it.

### Pseudocode

``` text
sort activities by finish time

select the first activity
previous_finish = finish of selected activity

for every remaining activity:
    if start[i] >= previous_finish:
        select activity i
        previous_finish = finish[i]
```

### Why the greedy choice makes sense

Choosing the activity that finishes earliest leaves the **maximum
remaining time** for the activities that come after it.

This is the key greedy insight behind the Activity Selection Problem.

------------------------------------------------------------------------

# 7. A Simple Coin-Change Example

Consider an **infinite supply** of the following coins:

``` text
10, 5, 2, 1
```

Suppose we need to make:

``` text
Amount = 52
```

A natural greedy strategy is:

> **Always take the largest coin that does not exceed the remaining
> amount.**

The process is:

``` text
52
↓ take 10
42
↓ take 10
32
↓ take 10
22
↓ take 10
12
↓ take 10
2
↓ take 2
0
```

So:

``` text
52 = 10 + 10 + 10 + 10 + 10 + 2
```

Number of coins:

``` text
6
```

For this particular coin system, the greedy strategy gives the minimum
number of coins.

### Greedy rule

``` text
Take the largest possible denomination first.
```

------------------------------------------------------------------------

# 8. Important: Greedy Does NOT Always Work

A very important point from the introduction is:

> **Greedy algorithms may not work always.**

Consider:

``` text
coins = {18, 1, 10}
amount = 20
```

If we greedily take the largest possible coin:

``` text
20
↓ take 18
remaining = 2
↓ take 1
remaining = 1
↓ take 1
remaining = 0
```

We use:

``` text
18 + 1 + 1
```

Total coins:

``` text
3
```

But a better solution is:

``` text
10 + 10 = 20
```

Total coins:

``` text
2
```

So the greedy choice **fails to produce the optimal solution**.

### Lesson

The fact that a choice looks best at the current moment does **not**
automatically mean it is part of the global optimum.

You must know that the problem has the required greedy structure.

------------------------------------------------------------------------

# 9. Another Example Where Greedy Can Fail: Longest Path

The introduction also highlights the **Longest Path** problem as an
example where simply making the locally best choice is not generally
enough.

Imagine a weighted graph where, at each node, one outgoing edge looks
better because it has a larger immediate weight.

A greedy strategy might therefore choose:

``` text
current node
    ↓
largest-looking edge
    ↓
largest-looking edge
    ↓
...
```

But the edge with the largest immediate weight can lead to a poor
continuation, while a smaller initial edge may lead to a much longer
overall path.

### Lesson

For problems such as **Longest Path**, a locally best decision does not
necessarily produce the globally best path.

So:

> **Do not assume that an optimization problem can be solved greedily
> just because a greedy choice is easy to define.**

------------------------------------------------------------------------

# 10. Applications of Greedy Algorithms

Greedy algorithms are commonly used for finding optimal solutions in
problems where the greedy-choice property holds.

### Finding Optimal Solutions

Examples include:

-   **Activity Selection**
-   **Fractional Knapsack**
-   **Job Sequencing**
-   **Prim's Algorithm**
-   **Kruskal's Algorithm**
-   **Dijkstra's Algorithm**
-   **Huffman Coding**

### Finding Close-to-Optimal Solutions

Greedy methods can also be used to find solutions that are **close to
optimal** for some difficult problems.

For example:

-   **Travelling Salesman Problem (TSP)**

TSP is an **NP-hard** problem, so finding the exact optimal solution
efficiently is difficult in general. A greedy heuristic can instead
produce a good/near-optimal solution quickly, depending on the strategy
used.

------------------------------------------------------------------------

# 11. Common Greedy Pattern

A useful way to recognize a greedy problem is to look for this
structure:

``` text
1. There is an optimization objective.
2. A decision has to be made repeatedly.
3. There is an obvious "best" choice at each step.
4. The choice can be made without revisiting previous choices.
5. The local choice can be proven to preserve global optimality.
```

Typical greedy criteria might be:

``` text
Maximum value
Minimum cost
Earliest finish time
Highest value/weight ratio
Smallest edge weight
Closest/cheapest next choice
```

The exact criterion depends entirely on the problem.

------------------------------------------------------------------------

# 12. Greedy vs. "Just Pick the Largest"

Greedy does **not** simply mean:

> "Always pick the largest number."

It means:

> **Choose the locally best option according to the problem-specific
> greedy criterion.**

Examples:

  -----------------------------------------------------------------------
  Problem                             Greedy Choice
  ----------------------------------- -----------------------------------
  Fractional Knapsack                 Highest value/weight ratio

  Activity Selection                  Earliest finishing compatible
                                      activity

  Coin Change (when greedy is valid)  Largest denomination not exceeding
                                      remaining amount

  Kruskal's Algorithm                 Smallest edge that does not create
                                      a cycle

  Prim's Algorithm                    Minimum-weight edge connecting the
                                      current tree to a new vertex

  Huffman Coding                      Combine two least-frequent nodes
  -----------------------------------------------------------------------

So the most important step in designing a greedy algorithm is
identifying the **correct greedy choice**.

------------------------------------------------------------------------

# 13. Greedy Algorithm Checklist

When you encounter a new optimization problem, ask:

### 1. What is the objective?

Are we trying to:

-   maximize something?
-   minimize something?
-   find the largest/smallest possible number?

### 2. What is the local choice?

What option looks best **right now**?

### 3. Is the choice always feasible?

Does choosing it violate any constraint?

### 4. Can the choice be made permanent?

If we select it now, do we ever need to undo it?

### 5. Does local optimality imply global optimality?

This is the most important question.

If the answer is **yes**, greedy may be appropriate.

If not, consider other paradigms such as:

-   Dynamic Programming
-   Backtracking
-   Divide and Conquer
-   Graph algorithms
-   Mathematical/optimization techniques

------------------------------------------------------------------------

# 14. Key Takeaways

-   **Greedy is an algorithmic paradigm** that builds a solution
    incrementally.
-   At each step, it chooses the **best-looking local option**.
-   Greedy is useful when **local optimal choices lead to a global
    optimum**.
-   A generic greedy algorithm repeatedly:
    -   selects an item,
    -   checks feasibility,
    -   adds it to the solution if feasible.
-   **Fractional Knapsack** works greedily using the highest
    `value/weight` ratio.
-   **Activity Selection** works greedily by selecting the compatible
    activity with the **earliest finish time**.
-   Greedy **does not always work**.
-   The coin set `{18, 1, 10}` with amount `20` demonstrates a case
    where greedy fails.
-   For difficult problems such as **TSP**, greedy methods may be used
    as heuristics to obtain a good/near-optimal solution.
-   The most important part of a greedy solution is not writing the loop
    --- it is identifying and justifying the **correct greedy choice**.

## One-line definition to remember

> **Greedy algorithm = repeatedly make the best locally available
> choice, hoping/knowing that these choices lead to the best global
> solution.**
