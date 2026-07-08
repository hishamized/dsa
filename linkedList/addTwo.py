from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = 0
        len2 = 0
        larger = None
        firstHead = l1
        secondHead = l2
        while firstHead is not None:
            len1+=1
            firstHead = firstHead.next
        while secondHead is not None:
            len2+=1
            secondHead = secondHead.next
        if len1>len2:
            larger = l1
        else:
            larger = l2
        firstHead = l1
        secondHead = l2
        carry = 0
        resultHead = None
        origin = None
        while firstHead is not None or secondHead is not None:
            if firstHead and secondHead:
                item = firstHead.val + secondHead.val + carry
                carry = 0
            if firstHead is not None and secondHead is None:
                item = firstHead.val + carry
                carry = 0
            if secondHead is not None and firstHead is None:
                item = secondHead.val + carry
                carry = 0
            if item <= 9:
                new_node = ListNode(item, None)
                if resultHead is None:
                    resultHead = new_node
                    origin = resultHead
                else:
                    resultHead.next = new_node
                    resultHead = resultHead.next
            if item > 9 and larger.next is not None:
                carry = item//10
                item = item%10
                new_node = ListNode(item)
                if resultHead is None:
                    resultHead = new_node
                    origin = resultHead
                else:
                    resultHead.next = new_node
                    resultHead = resultHead.next
            if item > 9 and larger.next is None:
                one = item % 10
                two = (item//10) % 10
                another_new_node = ListNode(two, None)
                new_node = ListNode(one, None)
                if resultHead is None:
                    resultHead = new_node
                    resultHead.next = new_node
                    origin = resultHead
                else:
                    resultHead.next = new_node
                    resultHead.next.next = another_new_node
                    resultHead = resultHead.next
            if firstHead:
                firstHead = firstHead.next
            if secondHead:
                secondHead = secondHead.next
            if larger:
                larger = larger.next
        return origin


# ---------- Helper functions for debugging ----------

def build_list(nums):
    dummy = ListNode()
    curr = dummy

    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def print_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# ---------- Test case ----------

l1 = build_list([5])
l2 = build_list([5])

sol = Solution()
answer = sol.addTwoNumbers(l1, l2)

print_list(answer)