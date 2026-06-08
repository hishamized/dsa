from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd_head = head
        final_head = odd_head
        even_head = odd_head.next
        og_even_head = even_head
        real_head = head.next.next
        real_index = 3
        while real_head is not None:
            if real_index % 2 == 0:
                even_head.next = real_head
                even_head = even_head.next
            else:
                odd_head.next = real_head
                odd_head = odd_head.next
            real_index += 1
            real_head = real_head.next
            odd_head.next = og_even_head
        else:
            even_head.next = None
        return final_head


# ---------------- Helpers for local testing ----------------

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


# ---------------- Run your test ----------------

head = build_list([1, 2, 3, 4, 5])

sol = Solution()
result = sol.oddEvenList(head)

print_list(result)

# NOTE: your original trailing text was invalid Python:
# "for Input: head = [1,2,3,4,5]"