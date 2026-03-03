def middle(head):
    if head is None:
        return None
    if head.next is None:
        return head
    curr = head
    count = 1

    while curr.next != None:
        count += 1
        curr = curr.next

    m = count // 2

    curr = head

    for _ in range(m):
        curr = curr.next
    
    return curr.data

# more efficient method

def mid(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data