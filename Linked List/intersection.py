# intersection of 2 linked list

def length_of_ll(head):
    count = 0
    if head == None:
        return 0
    
    curr = head

    while curr:
        count += 1
        curr = curr.next
    
    return count

def intersection(head_1, head_2):
    c1 = length_of_ll(head_1)
    c2 = length_of_ll(head_2)

    d = abs(c1 - c2)

    if c1 >= c2:
        curr1 = head_1
        curr2 = head_2
    elif c1 < c2:
        curr1 = head_2
        curr2 = head_1

    for _ in range(d):
        if curr1 == None:
            return None
        curr1 = curr1.next
    
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        
        curr1 = curr1.next
        curr2 = curr2.next
    
    return None