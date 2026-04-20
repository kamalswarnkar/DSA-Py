# Floyd's Cycle Detection in a linked list

def floyds_cycle_detection(head):
    slow, fast = head, head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

"""
Time Complexity: O(n + m)
n = length of loop, if any
m = length of linked list  before loop start
"""