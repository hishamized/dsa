from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_list(self,head, label=""):
        if label:
            print(f"\n{label}")

        temp = head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return
        temp = head
        while temp is not None:
            if head.val == val:
                target = temp
                head = target.next
                del target
                temp = temp.next
                continue
            if temp is not None and temp.next is not None and temp.next.val == val:
                target = temp.next
                temp.next = temp.next.next
                del target
                continue
            if temp is not None:
                temp = temp.next 
        return head

# Create linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

result = Solution().removeElements(head, 2)
temp = result
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")