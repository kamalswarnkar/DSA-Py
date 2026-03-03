# is sorted or not

def isSorted(self, head):
    curr = head
    inc = 1
    dec = 1
        
    while curr.next != None:
            
        if curr.next.data < curr.data:
            inc = 0
            break
            
        curr = curr.next
        
    curr = head
        
    while curr.next != None:
            
        if curr.next.data > curr.data:
            dec = 0
            break
            
        curr = curr.next
        
    if inc or dec:
        return True
        
    return False

# removing duplicates from a sorted linked list

def remove_duplicate(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    curr = head
    
    while curr and curr.next:
        if curr.key == curr.next.key:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head