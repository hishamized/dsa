class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def _handleHead(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            return True
        else:
            return False
    def display(self):
        if self.head is None:
            print("The doubly linked list has no head and is thus empty")
            return
        temp = self.head
        while True:
            print(temp.data , " --> ", end=" ")
            if temp.next is None:
                break
            temp=temp.next
        print()
    def prepend(self, data):
        if self._handleHead(data) == True:
            return
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        return
    def append(self, data):
        if self._handleHead(data) == True:
            return
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.next = None
        new_node.prev = temp
        return
    def insert_at(self, data, target):
        if self._handleHead(data) == True:
            return
        new_node = Node(data)
        pos = -1
        temp = self.head
        if target == 0:
            new_node.next = temp
            new_node.prev = None
            temp.prev = new_node
            self.head = new_node
            return
        while temp.next is not None:    
            pos += 1
            if pos + 1 == target:
                ahead = temp.next
                new_node.next = ahead
                new_node.prev = temp
                temp.next = new_node
                ahead.prev = new_node
                break
            temp = temp.next
    def delete_first(self):
        if self.head is None:
            print("The doubly linked list is empty and thus there is nothing to delete")
            return
        temp = self.head
        self.head = temp.next
        print(f"Successfully deleted node with data {temp.data}")
        del temp
        return
    def delete_last(self):
        if self.head is None:
            print("The doubly linked list is empty and thus there is nothing to delete")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        behind = temp.prev
        behind.next = None
        print(f"Successfully deleted node with data {temp.data}")
        del temp
    def delete_at_index(self, target):
        if self.head is None:
            print("The doubly linked list is empty and thus there is nothing to delete")
            return
        pos = -1
        temp = self.head
        if target == 0:
            ahead = temp.next
            ahead.prev = None
            print(f"Successfully deleted node with data {temp.data}")
            self.head = ahead
            del temp
            return
        while temp.next is not None:    
            pos += 1
            if pos  == target:
                ahead = temp.next
                behind = temp.prev
                ahead.prev = behind
                behind.next = ahead
                print(f"Successfully deleted node with data {temp.data}")
                del temp
                break
            temp = temp.next
    def delete_by_value(self, target):
        if self.head is None:
            print("The doubly linked list is empty and thus there is nothing to delete")
            return
        pos = -1
        temp = self.head
        if target == temp.data:
            ahead = temp.next
            ahead.prev = None
            print(f"Successfully deleted node with data {temp.data}")
            self.head = ahead
            del temp
            return
        while temp.next is not None:    
            if temp.data  == target:
                ahead = temp.next
                behind = temp.prev
                ahead.prev = behind
                behind.next = ahead
                print(f"Successfully deleted node with data {temp.data}")
                del temp
                break
            temp = temp.next
    def search_by_value(self, target):
        if self.head is None:
            print("The doubly linked list is empty")
            return
        temp = self.head
        pos = 0
        found = False
        while temp.next is not None:
            if temp.data == target:
                print(f"Found the {target} at index {pos} having value {temp.data}")
                found = True
                break
            temp = temp.next
            pos += 1
        if not found:
            print("Could not find the element {target} in the list")
list = DoublyLinkedList()
list.prepend(3)
list.prepend(2)
list.prepend(1)
list.append(4)
list.append(5)
list.append(6)
list.insert_at(1000, 0)
list.display()
list.delete_first()
list.display()
list.delete_last()
list.display()
list.delete_at_index(2)
list.display()
list.delete_by_value(4)
list.display()
list.append(6)
list.append(7)
list.append(8)
list.display()
list.search_by_value(7)