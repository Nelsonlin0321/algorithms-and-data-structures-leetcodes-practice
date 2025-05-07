# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_number_node(head: ListNode):
    num = 0

    while head:
        num += 1
        head = head.next

    return num


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        k = get_number_node(head)
        j = k - n

        if j == 0:
            #  need to delete the first node:
            return head.next

        curr = head
        for _ in range(j-1):
            curr = curr.next

        node_to_delete = curr.next
        curr.next = node_to_delete.next
        node_to_delete.next = None

        return head


def getNthFromEnd(head: ListNode, n: int) -> ListNode:
    fast = head
    for _ in range(n):
        if fast is None:
            #  the node before N is empty, which mean the node to delete is the first node
            return None
        fast = fast.next

    slow = head
    while fast:
        fast = fast.next
        slow = slow.next

    return slow


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeBeforeN = getNthFromEnd(head, n+1)
        if nodeBeforeN is None:
            return head.next
        nodeBeforeN.next = nodeBeforeN.next.next
        return head


class Solution:
    # 主函数
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 虚拟头结点: In case the node to be deleted is the first node.
        dummy = ListNode(-1)
        dummy.next = head
        # 删除倒数第 n 个，要先找倒数第 n + 1 个节点
        x = self.findFromEnd(dummy, n + 1)
        # 删掉倒数第 n 个节点
        x.next = x.next.next
        return dummy.next

    # 返回链表的倒数第 k 个节点
    def findFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        # p1 先走 k 步
        for i in range(k):
            p1 = p1.next
        p2 = head
        # p1 和 p2 同时走 n - k 步
        while p1:
            p2 = p2.next
            p1 = p1.next
        # p2 现在指向第 n - k 个节点
        return p2


if __name__ == "__main__":
    pass
