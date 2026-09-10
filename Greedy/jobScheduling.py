"""
Job Sequencing with Deadlines

Given a set of jobs, where each job has:
    • A deadline
    • A profit

Every job takes exactly one unit of time.

Schedule jobs so that:
    • Each job is completed on or before its deadline.
    • At most one job is performed in a time slot.
    • Total profit is maximized.

Greedy Strategy:
1. Sort all jobs by decreasing profit.
2. For each job, try to place it in the latest available
   time slot before or at its deadline.
3. If a suitable slot is found, schedule the job and add
   its profit.

Why the latest available slot?
    Placing a job as late as possible leaves earlier slots
    available for jobs with tighter deadlines.

Method I:
    Basic Greedy + Slot Scanning

Method II:
    Optimized Greedy + Disjoint Set Union (DSU)

Time Complexity:
    Method I : O(N log N + N × D)
               O(N²) in the worst case when D <= N.

    Method II: O(N log N)

Space Complexity:
    O(N)

where,
N = number of jobs
D = maximum deadline

Note:
• Each job takes exactly one unit of time.
• `arr[i]` is represented as [deadline, profit].
• The input array is sorted in-place.
• Both methods use the same greedy strategy.
• Method II optimizes the process of finding an available slot.
"""

def jobScheduling(arr):
    n = len(arr)
    res = 0

    # `scheduled[slot]` tells whether a time slot is occupied.
    # Slot 0 is unused; slots 1 to n represent possible
    # execution times.
    
    scheduled = [False] * n

    arr.sort(key = lambda x : x[1], reverse = True)

    for deadline, profit in arr:
        for slot in range(min(n, deadline), 0, -1):
            if not scheduled[slot]:
                scheduled[slot] = True
                res += profit
                break

    return res

# optimized method

def jobScheduling(arr):
    n = len(arr)
    res = 0 # total profit

    # for getting both total profit, and total jobs
    # res_j, res_p = 0, 0
    
    scheduled = [False] * n

    arr.sort(key = lambda x : x[1], reverse = True)

    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    for deadline, profit in arr:
        slot = find(min(n, deadline))

        if slot > 0:
            res += profit
            # res_p += profit
            # res_j += 1
            parent[slot] = find(slot - 1)
    
    return res #[res_j, res_p]