class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Stack:
    """A stack is a collection of objects that are inserted and removed
    according to the last-in, first-out (LIFO) principle.

    A user may insert objects into a stack at any time,
    but may only access or remove the most recently inserted object
    that remains (at the so-called 'top' of the stack).

    LIFO Stack implementation using a Python list as underlying storage.
    """

    def __init__(self):
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack.
        Time Complexity: O(1)
        """
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty.
        Time Complexity: O(1)
        """
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack.
        Time Complexity: O(1)
        """
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()  # remove last item from list


class Queue:
    """A queue is a close “cousin” of the stack, as a queue is a collection of objects
    that are inserted and removed according to the first-in, first-out (FIFO) principle.
    That is, elements can be inserted at any time,
    but only the element that has been in the queue the longest can be next removed.

    FIFO queue implementation using a Python list as underlying storage
    """
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned
