
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

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
    #YOUR CODE GOES HERE
    """
    Given a singly linked list, modify the list in place so that all
    all evening indexed nodes come before all oddly indexed nodes (where the 
    index obviously starts at the even number 0), but otherwise they are in 
    the same order.

    parameters
    ----------
        head: the head element of a linked list
    
    returns
    -------
        The head element of the same linked list, but modified.
    """    

    # It would be better to move this function outside of the function, but I
    # don't know if this is allowed.
    def split_linked_list(head):
        """
        Splits a linked list into a two parts.  An odd and even part.

        Returns the heads and tails of each part.

        parameters
        ----------
            head: the head element of a linked list
        returns
        -------
            A 4-tuple containing:
                - The head element of the even linked list.
                - The head element of the odd linked list.
                - The tail element of the even linked list.
                - The tail element of the odd linked list.
        """

        if head.next is None:
            return head, None, head, None
        
        if head.next.next is None:
            return head, head.next, head, head.next
        
        head_even = head.next
        head_odd, _, tail_odd, tail_even = split_linked_list(head_even)

        return head_even, head_odd, tail_even, tail_odd

    _, head_odd, tail_even, _ = split_linked_list(head)
    tail_even.next = head_odd

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