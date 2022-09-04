# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        curr = head
        prev = None
        for _ in range(n):
            fast = fast.next

        while (fast is not None):
            prev = curr
            curr = curr.next
            fast = fast.next

        if prev is None:  # prev 是空的话， 说明移除的Node 是在第一个位置上，所以我们只需要把 head.next 返回
            return curr.next
        else:
            prev.next = curr.next  # 把head 中的 prev.next 指向 curr.next
        return head



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        
        for _ in range(n+1):
            if fast:
                fast = fast.next
            else:
                return head.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next.next
        slow.next = temp
        
        return head

        

if __name__ == "__main__":
    pass

