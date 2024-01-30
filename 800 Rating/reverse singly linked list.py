class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, value):
        if self.head is None:
            return

        if self.head.val == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.val == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, end="->")
            current = current.next
        print()
    def reverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev



my_list = LinkedList()

# Append some elements
my_list.append(1)
my_list.append(2)
my_list.append(3)




my_list.display()
my_list.reverse()
my_list.display()# Output: 0 1 2 3

