
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""

#constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvenList_Helper(head):
    current = head
    
    # save head of the list of evens
    evens_head = head.next
    
    counter = 1
    
    # until you reach the last node
    while current.next is not None:
        nxt = current.next
        
        if nxt.next is not None:
            # change the next node to the next-next node
            current.next = nxt.next

        # When you get to second to last node (ie nxt.next is None:)
        else:        
            # if current node is even, then it will be the tail
            if counter % 2 == 0:
                # so change next to None
                current.next = None # or = nxt.next
                # and change the last node to head of evens
                nxt.next = evens_head
                break
            
            # if current node is odd, it should join to head of evens
            if counter % 2 == 1:
                current.next = evens_head

        # traverse to next node
        current = nxt
        
        counter += 1
        
    return head


#DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


#test case
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head =  oddEvenList(head)
    print ("Expected result: 1, 3, 5, 2, 4")
    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))

if __name__ == "__main__":
    main()