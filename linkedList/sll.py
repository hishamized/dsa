class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        new_node.next = None
        self.head = new_node
    def insert_at_beginning(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            new_node.next = None
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    def insert_after_node(self, target, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            found = False
            temp = self.head
            while(temp.next):
                if temp.data == target:
                    found = True
                    utility = temp.next
                    temp.next = new_node
                    new_node.next = utility
                    break
                temp = temp.next
            if not found:
                print("Could not find any node with such data")
    def insert_before_node(self, target, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
        elif self.head.data == target:
            found = True
            new_node = Node(data)
            utility = self.head
            new_node.next = utility
            self.head = new_node  
        else:
            found = True
            temp = self.head.next
            prev = self.head
            while(temp.next):
                if temp.data == target:
                    fount = True
                    new_node = Node(data)
                    prev.next = new_node
                    new_node.next = temp
                    break
                prev = prev.next
                temp = temp.next
        if not found:
            print("Could not find any node with data ", target)
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        tail = self.head
        while tail.next != None:
            tail = tail.next
        tail.next = new_node
    def insert_at_position(self, pos, data):
        if self.head is None:
            new_node= Node(data)
            self.head = new_node
        else:
            index = 0
            temp = self.head
            while(temp.next):
                if pos == index + 1:
                    new_node = Node(data)
                    utility = temp.next
                    temp.next = new_node
                    new_node.next = utility
                    break
                else:
                    index += 1
                    temp = temp.next
    def display_list(self):
        temp = self.head
        while True:
            print(f"{temp.data} --> ", end=" ")
            temp = temp.next
            if temp is None:
                break
        print()
    def delete_node_by_data(self, target):
        head = self.head
        if head.data == target:
            swap = head.next
            self.head = swap
        else:
            temp = self.head
            prev = None
            while temp.next != None:
                prev = temp
                temp = temp.next
                if temp.data == target:
                    prev.next = temp.next
                    temp.next = None

    def delete_first_node(self):
        if self.head is None:
            print("The linked list is empty and there is nothinng to delete")
            return
        else:
            temp = self.head
            self.head = temp.next
            del temp
            return
    def delete_last_node(self):
        if self.head is None:
            print("The linked list is empty and there is nothing to delete")
            return
        else:
            temp = self.head.next
            prev = self.head
            while(temp.next):
                temp = temp.next
                prev = prev.next
            prev.next = None
            del temp
            return
    def delete_by_index(self, pos):
        if self.head is None:
            print("There is no element in the linked list.")
            return
        else:
            index = 0
            temp = self.head
            while(temp.next):
                if index + 1 == pos:
                    target = temp.next
                    temp.next = target.next
                    target.next = None
                    del target
                temp = temp.next
                index += 1
list = SinglyLinkedList(4)
list.insert_at_beginning(3)
list.insert_at_beginning(2)
list.insert_at_beginning(1)
list.display_list()
list.insert_at_end(5)
list.display_list()
list.delete_node_by_data(1)
list.display_list()
list.delete_node_by_data(4)
list.display_list()
list.insert_after_node(3,4)
list.display_list()
list.insert_before_node(4, 10)
list.display_list()
list.insert_after_node(2,20)
list.display_list()
list.insert_at_position(2, 999)
list.display_list()
list.delete_first_node()
list.display_list()
list.delete_last_node()
list.display_list()
list.delete_by_index(2)
list.display_list()