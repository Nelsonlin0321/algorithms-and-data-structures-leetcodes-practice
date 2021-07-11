from data_structure import ListNode
from data_structure import LinkedList




# iterative method
class Solution:
    """
    # Runtime: 32 ms, faster than 87.75% of Python3 online submissions for Reverse Linked List.
    # Memory Usage: 15.6 MB, less than 43.00% of Python3 online submissions for Reverse Linked List.
    """
    def reverseList(self, head: ListNode) -> ListNode:
        # define pointers

        prev, curr = None, head

        while curr:
            # get and save the next
            next = curr.next

            # reserve
            curr.next = prev

            # update the position
            prev = curr
            curr = next

        # prev is the all nodes that we're reversed
        return prev


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    reversed_linked_list = LinkedList()(head)



