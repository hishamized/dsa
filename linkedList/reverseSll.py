from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        nodes = []
        temp = head
        nodes.append(temp)

        while temp.next is not None:
            length += 1
            temp = temp.next
            nodes.append(temp)

        l = len(nodes)
        rev_head = nodes.pop(l-1)
        rev_head.next = None

        temp = rev_head

        while length > 1:
            l = len(nodes)
            item = nodes.pop(l-1)
            item.next = None
            temp.next = item
            temp = temp.next
            length -= 1

        return rev_head


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head, limit=20):
    current = head
    count = 0

    while current is not None and count < limit:
        print(current.val, end=" -> ")
        current = current.next
        count += 1

    if current is not None:
        print("...")
    else:
        print("None")


tests = [
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4, 5]
]

sol = Solution()

for test in tests:
    print("\nInput:")
    head = create_linked_list(test)
    print_linked_list(head)

    result = sol.reverseList(head)

    print("Output:")
    print_linked_list(result)