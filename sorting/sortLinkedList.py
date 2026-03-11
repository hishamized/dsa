# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def sortList(self, head):
        minPointer = None
        newHead = head
        while newHead:
            slider = newHead
            min = slider.val
            while slider:
                if slider.val <= min:
                    min = slider.val
                    print("Minimum inside loops : ", min)
                    minPointer = slider
                slider = slider.next
            print(f"Minimum outside loop: {min}")
            temp = newHead.val
            newHead.val = min
            print(f"Minpointer value before swap: {minPointer.val}")
            minPointer.val = temp
            printList(head)
            newHead = newHead.next
        else:
            return head

def printList(head):
    while head:
        print(head.val, end=" - ")
        head = head.next
head = None 
tail = None
for i in range(1,5):
   newNode = ListNode(5-i)
   if head is None:
       head = newNode
       tail = newNode
   else:
        tail.next = newNode
        tail = newNode
# printList(head)
sol = Solution()
sol.sortList(head)
# printList(head)

        