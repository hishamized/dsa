from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        history = []
        temp = head
        tail = head
        counter = 0
        while tail is not None:
            history.append(tail)
            tail = tail.next
        while history:
            temp = history[counter]
            tail = history.pop()
            lastIndex = len(history) - 1
            if temp == tail or temp.next == tail:
                break
            manzim = history[counter + 1]
            temp.next = tail
            tail.next = manzim
            last = history[lastIndex]
            last.next = None
            counter += 1
            print_linked_list(head)

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next


# ---------------- Test Case 1 ----------------
head = create_linked_list([1, 2, 3, 4])

print("Before:")
print_linked_list(head)

Solution().reorderList(head)

print("After:")
print_linked_list(head)


# ---------------- Test Case 2 ----------------
head = create_linked_list([1, 2, 3, 4, 5])

print("\nBefore:")
print_linked_list(head)

Solution().reorderList(head)

print("After:")
print_linked_list(head)