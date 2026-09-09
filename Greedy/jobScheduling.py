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

Time Complexity:
    O(N log N + N × D)

    where:
        N = number of jobs
        D = maximum deadline

    Since D <= N in the usual formulation:
        O(N²) in the worst case.

Space Complexity:
    O(N)

Note:
• Each job takes exactly one unit of time.
• `arr[i]` is represented as [deadline, profit].
• The input array is sorted in-place.
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