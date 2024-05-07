class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode: Node = Node(data)
        if self.tail is None:
            self.head: Node = newNode
            self.tail: Node = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
        if self.tail is None:
            self.tail = self.head

    def display(self):
        iterator = self.head
        print("None <-->", end=" ")
        while iterator is not None:
            print(iterator.data, "<-->", end=" ")
            iterator = iterator.next
        print("None")

    def remove(self, value):
        iterator = self.head
        if self.head is None:
            return
        elif self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            while iterator.next:
                if iterator.next.data == value:
                    iterator.next = iterator.next.next
                    if iterator.next:
                        iterator.next.prev = iterator
                    else:
                        self.tail = iterator
                    break
                iterator = iterator.next

    def size(self):
        index: int = 0
        iterate = self.head
        while iterate:
            index += 1
            iterate = iterate.next

        return index

    def isEmpty(self):
        return self.head is None

    def insert(self, index, data):
        if index < 0 or index > self.size():
            raise Exception(" Enter the Correct Index")
        if index == 0:
            self.prepend(data)
        else:
            newNode = Node(data)
            iterator = self.head
            for _ in range(index-1):
                iterator = iterator.next
            newNode.next = iterator.next
            newNode.prev = iterator
            if iterator.next:
                iterator.next.prev = newNode
            iterator.next = newNode
            if not newNode.next:
                self.tail = newNode

    def reverse(self):
        curr = self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev
        self.head, self.tail = self.tail, self.head

    # Additional feature: method to display the list in reverse order
    def display_reverse(self):
        iterator = self.tail
        print("None <-->", end=" ")
        while iterator is not None:
            print(iterator.data, "<-->", end=" ")
            iterator = iterator.prev
        print("None")


dll = DoublyLinkedList()
dll.append(90)
dll.append(80)
dll.append(70)
dll.append(60)
dll.display()
dll.remove(60)
dll.display()
print("tail value --> ", dll.tail.data)
print(dll.size())
print(dll.isEmpty())
emp = DoublyLinkedList()
print(emp.size())
print(emp.isEmpty())
dll.insert(index=0, data=99)
dll.insert(index=4, data=50)
dll.display()
print("tail value --> ", dll.tail.data)
dll.reverse()
dll.display()
print("Head value --> ", dll.head.data)
print("tail value --> ", dll.tail.data)
dll.display_reverse()
