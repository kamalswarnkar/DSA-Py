# Finding the maximum of subarray of size 'k' using Sliding Window Maximum Algorithm with Monotonic Queue

from collections import deque

def printMax(arr, k):
    n = len(arr)
    dq = deque()

    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    print(arr[dq[0]], end=" ")

    for i in range(k, n):
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        
        dq.append(i)

        print(arr[dq[0]], end=" ")