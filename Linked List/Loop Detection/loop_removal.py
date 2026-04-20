def remove_loop(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    
    if slow != fast:
        return 
    
    slow = head
    
    # special case where loop starts at head

    if slow == fast:
        while fast.next != slow:
            fast = fast.next
        fast.next = None

        return
    
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None   