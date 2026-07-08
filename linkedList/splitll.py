from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------- Your Solution ----------
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head
        sizePerPart = 0
        firstNPartsWithExtra = 0
        result = []
        while temp is not None:
            temp = temp.next
            length += 1
        sizePerPart = length // k
        firstNPartsWithExtra = length % k
        temp = head
        for i in range(1, k + 1):
            if i > length:
                result.append(None)
                continue
            if i <= firstNPartsWithExtra:
                result.append(temp)
                for i in range(1, sizePerPart + 2):
                    if i == sizePerPart + 1:
                        x = temp.next
                        temp.next = None
                        temp = x
                        continue
                    temp = temp.next
            else:
                result.append(temp)
                for i in range(1, sizePerPart + 1):
                    if i == sizePerPart:
                        x = temp.next
                        temp.next = None
                        temp = x
                        continue
                    temp = temp.next
        return result


# ---------- Build input list: 1 -> 2 -> 3 -> ... -> 10 ----------
head = ListNode(1)
current = head

for i in range(2, 11):
    current.next = ListNode(i)
    current = current.next

k = 5

# ---------- Run ----------
sol = Solution()
parts = sol.splitListToParts(head, k)

# ---------- Print ----------
for idx, part in enumerate(parts):
    print(f"Part {idx}:", end=" ")
    curr = part
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")