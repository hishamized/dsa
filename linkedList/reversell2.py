from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head is None:
            return None

        if head.next is None:
            return head

        if left == right:
            return head

        mainCount = 1
        subCount = 0
        nodes = []

        behind = None
        ahead = head

        linker1 = None
        linker2 = None
        newHead = None
        newTail = None
        temp = None

        while ahead is not None:

            if mainCount == left:
                linker1 = behind
                newHead = ahead

            if mainCount == right:
                linker2 = ahead.next
                newTail = ahead
                break

            behind = ahead
            ahead = ahead.next
            mainCount += 1

        temp = newHead

        while temp != linker2:
            nodes.append(temp)
            temp = temp.next
            subCount += 1

        rev_head = nodes.pop()
        rev_head.next = None
        temp = rev_head

        if linker1 is None:
            head = temp
        else:
            linker1.next = temp

        while nodes:
            item = nodes.pop()
            item.next = None
            temp.next = item
            temp = temp.next

        temp.next = linker2

        return head

# ---------------- DRIVER ----------------

def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def print_list(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)


head = build_list([1, 2, 3, 4, 5])

left = 2
right = 4

sol = Solution()
result = sol.reverseBetween(head, left, right)

print_list(result)