class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.front
        queue_str = ""
        while current:
            queue_str += str(current.data) + " -> "
            current = current.next
        return queue_str + "None"


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue)  # Outputs: Queue: 1 -> 2 -> 3 -> None
print("Queue size:", len(queue))  # Outputs: Queue size: 3
print("Peek:", queue.peek())  # Outputs: Peek: 1
print("Dequeue:", queue.dequeue())  # Outputs: Dequeue: 1
queue.enqueue(9)
print("Queue:", queue)  # Queue: 2 -> 3 -> 9 -> None
print("Dequeue:", queue.dequeue())  # Outputs: Dequeue: 2
# Outputs: Queue after dequeue: 2 -> 3 -> None
print("Queue after dequeue:", queue)
