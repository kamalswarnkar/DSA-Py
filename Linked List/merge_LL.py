"""
merging 2 linked lists
without using any extra 
auxiliary space, i.e.,
Auxiliary Space Complexity = O(1)
Time Complexity = O(n + m);
where-> n, m are lengths of 1st and 2nd linked
list respectively
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