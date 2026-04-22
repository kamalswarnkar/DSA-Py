"""
merging n sorted linked lists contained in an
array into one single sorted linked list.

One of best approach is Divide and Conquer,
where a pair of LL can be merged one by one
throughout the array.

Merge lists in pairs
Reduce K → K/2 → K/4 → ... → 1

Time Complexity: O(n*log(k)); n = total no. of nodes throughout all LLs,
k = length of array
"""

def merge(a, b):
    if a == None:
        return b
    
    if b == None:
        return a
    
    head, tail = None, None

    if a.data <= b.data:
        head = tail = a
        a = a.next
    else:
        head = tail = b
        b = b.next
    
    while a != None and b != None:
        if a.data <= b.data:
            tail.next = a
            tail = a
            a = a.next
        else:
            tail.next = b
            tail = b
            b = b.next
    
    if a == None:
        tail.next = b
    else:
        tail.next = a
    
    return head

def mergeKLists(arr):
    if len(arr) == 0:
        return None
        
    while len(arr) > 1:
        merged = []
        for i in range(0, len(arr), 2):
            a = arr[i]
            if i + 1 < len(arr):
                b = arr[i+1]
            else:
                b = None
                    
            merged.append(merge(a, b))
            
        arr = merged
        
    return arr[0]    