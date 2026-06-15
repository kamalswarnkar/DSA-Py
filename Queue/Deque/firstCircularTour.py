"""
    PROBLEM: You have a circle of petrol stations. Each station has a certain amount 
    of gas, and there is a specific distance to the next station. You need to find 
    the exact station to start at so that a truck can complete the full circle 
    without running out of gas.

    APPROACH: 
    We treat the route as a continuous loop and use a "two-pointer" strategy to 
    find the starting point efficiently:
    1. Start at the first station and keep track of your remaining gas.
    2. If at any point your gas drops below zero, it means your current starting 
    point (and all stations checked since then) cannot complete the loop.
    3. Skip all those stations, move your starting point to the next available 
    station, and reset your gas tank to zero.
    4. Keep a running total of the "deficit" (gas lost) to ensure that by the 
    end, the total gas available is at least equal to the total distance.

    Complexity: This checks each station at most twice, making it very fast (O(N)).
    
    Time: O(N)
    Space: O(1)
"""

def printTour(petrol, dist):
    n = len(petrol)

    start = 0
    curr_petrol = 0
    prev_petrol = 0

    for i in range(n):
        curr_petrol += (petrol[i] - dist[i]) # total petrol at station 'i'

        if curr_petrol < 0: # current station can be valid first station
            start = i + 1 # jump to next station directly
            prev_petrol += curr_petrol # save the gain/loss of petrol 
            curr_petrol = 0
        
    return (start + 1) if (curr_petrol + prev_petrol) >= 0 else -1