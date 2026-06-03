from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        h1 = list1
        h2 = list2
        dummy = ListNode(0)
        h3 = dummy
        while h1 is not None and h2 is not None:
            if h1 is None or h2 is None:
                break
            if h1.val > h2.val:
                h3.next = h2
                h3 = h3.next
                h2 = h2.next

            elif h2.val > h1.val:
                h3.next = h1
                h3 = h3.next
                h1 = h1.next

            else:
                h3.next = h1
                h1 = h1.next
                h3 = h3.next

                h3.next = h2
                h2 = h2.next
                h3 = h3.next
        if h1 is None and h2 is not None:
            while h2 is not None:
                h3.next = h2
                h3 = h3.next
                h2 = h2.next
            return dummy.next
        if h2 is None and h1 is not None:
            while h1 is not None:
                h3.next = h1
                h3 = h3.next
                h1 = h1.next
            return dummy.next
        '''
        if h1.next == None and h2.next == None:
            if h1.val > h2.val:
                h3.next = h2
                h3 = h3.next
                h3.next = h1
                h3 = h3.next
                return dummy.next
            if h2.val > h1.val:
                h3.next = h1
                h3 = h3.next
                h3.next = h2
                h3 = h3.next
                return dummy.next
            h3.next = h1
            h3 = h3.next
            h3.next = h2
            h3 = h3.next
            return dummy.next
        if h1.next == None and h2.next is not None:
            while h2.next is not None:
                h3.next = h2
                h3 = h3.next
                h2 = h2.next
            return dummy.next
        if h2.next == None and h1.next is not None:
            while h1.next is not None:
                h3.next = h1
                h3 = h3.next
                h1 = h1.next
            return dummy.next
       '''
        return dummy.next
def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" -> ".join(result))


# Test data
# list1 = build_linked_list([-9,3])
# list2 = build_linked_list([5,7])


# list1 = build_linked_list([-9,3])
# list2 = build_linked_list([5,7])

# list1 = build_linked_list([2,4,6,8,10,12,12,14])
# list2 = build_linked_list([1,3,5,7,9,11])

list1 = build_linked_list([-9,-5,-3,-2,-2,3,7])
list2 = build_linked_list([-10,-8,-4,-3,-1,3])

# Run
sol = Solution()
result = sol.mergeTwoLists(list1, list2)

# Print result
print_linked_list(result)