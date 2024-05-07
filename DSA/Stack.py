class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.top
        stack_str = ""
        while current:
            stack_str += str(current.data) + " -> "
            current = current.next
        return stack_str + "None"


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack)  # Outputs: Stack: 3 -> 2 -> 1 -> None
print("Stack size:", len(stack))  # Outputs: Stack size: 3
print("Peek:", stack.peek())  # Outputs: Peek: 3
print("Pop:", stack.pop())  # Outputs: Pop: 3
print("Stack after pop:", stack)  # Outputs: Stack after pop: 2 -> 1 -> None


'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return "->".join(map(str, self.stack[::-1])) + "->None"

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack)  # Outputs: Stack: 3->2->1->None
print("Stack size:", len(stack))  # Outputs: Stack size: 3
print("Peek:", stack.peek())  # Outputs: Peek: 3
print("Pop:", stack.pop())  # Outputs: Pop: 3
print("Stack after pop:", stack)  # Outputs: Stack after pop: 2->1->None

'''
