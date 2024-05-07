class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = self.head

    def display(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data, "-->", end=" ")
            iterator = iterator.next
        print("None")

    def remove(self, value):
        iterator = self.head
        if self.head is None:
            return
        elif self.head.data == value:
            self.head = self.head.next
        else:
            while iterator.next:
                if iterator.next.data == value:
                    iterator.next = iterator.next.next
                    if not iterator.next:
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
        # return self.size() is 0

    def insert(self, index, data):
        if index < 0 or index > self.size():
            raise Exception(" Enter the Correct Index")
        if index is 0:
            self.prepend(data)
        else:
            newNode = Node(data)
            iterator = self.head
            for _ in range(index-1):
                iterator = iterator.next
            newNode.next = iterator.next
            iterator.next = newNode
            if not newNode.next:
                self.tail = newNode

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.tail = self.head
        self.head = prev


ll = LinkedList()
ll.append(90)
ll.append(80)
ll.append(70)
ll.append(60)
ll.display()
ll.remove(60)
ll.display()
print("tail value --> ", ll.tail.data)
print(ll.size())
print(ll.isEmpty())
emp = LinkedList()
print(emp.size())
print(emp.isEmpty())
ll.insert(index=0, data=99)
ll.insert(index=4, data=50)
ll.display()
print("tail value --> ", ll.tail.data)
ll.reverse()
ll.display()
print("Head value --> ", ll.head.data)
print("tail value --> ", ll.tail.data)


'''
# Introduction to Linked Lists in Python

In this blog post, we'll dive into the concept of linked lists and explore how to implement them in Python. Linked lists are a fundamental data structure consisting of a sequence of elements, each connected to the next by pointers or references. They offer dynamic memory allocation and efficient insertion and deletion operations compared to arrays.

## What is a Linked List?

A linked list is a linear data structure where elements are not stored at contiguous memory locations like arrays. Instead, each element, called a node, comprises two parts: the data and a reference to the next node in the sequence. The last node typically points to `None`, indicating the end of the list.

## Types of Linked Lists

There are several types of linked lists:

1. **Singly Linked List**: Each node contains data and a reference to the next node.
2. **Doubly Linked List**: Each node contains data and references to both the next and previous nodes.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

For this tutorial, we'll focus on implementing a singly linked list in Python.

## Implementing a Singly Linked List in Python

Let's start by defining a `Node` class representing individual nodes of the linked list. Each node will have two attributes: `data` to store the element and `next` to reference the next node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```


Next, we'll create a `LinkedList` class to manage the nodes. It will have methods to perform various operations like insertion, deletion, traversal, and searching.

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

Now, let's demonstrate some basic operations on the linked list:

```python
# Create a new linked list
linked_list = LinkedList()

# Append elements to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Display the linked list
linked_list.display()
```

This will output:

```
1 -> 2 -> 3 -> None
```

## Conclusion

Linked lists are powerful data structures with various applications in computer science. In this tutorial, we covered the basics of implementing a singly linked list in Python and performing common operations like insertion and traversal. Feel free to experiment further and explore more advanced operations and variations of linked lists. Happy coding!

'''
