"""
Maximum Activity Selection

Select the maximum number of activities that can be performed
by a single person, assuming that a person can only work on
one activity at a time.

Idea:
1. Sort activities by their finish time.
2. Select the activity that finishes earliest.
3. For every remaining activity:
   • If its start time is >= the finish time of the previously
     selected activity, select it.
4. Continue until all activities are processed.

Greedy Choice:
    Always choose the activity with the earliest finish time.

Time Complexity:
    O(N log N)

Space Complexity:
    O(1) auxiliary space
    (ignoring the sorting implementation)

where,
N = number of activities

Note:
• Activities are represented as [start, finish].
• Activities with start time equal to the previous finish time
  are allowed.
"""


def maxActivity(arr):
    if not arr:
        return 0
    
    n = len(arr)
    arr.sort(key = lambda x : x[1])

    prev, res = 0, 1

    for curr in range(1, n):
        if arr[curr][0] >= arr[prev][1]:
            prev = curr
            res += 1

    return res