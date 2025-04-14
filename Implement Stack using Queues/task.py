""" Implement Stack using Queues """

class Queue:
    """ Queue """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


class MyStack(object):
    """ My Stack """
    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while not self.first_queue.is_empty():
            self.second_queue.add(self.first_queue.pop())
        self.first_queue.add(x)
        while not self.second_queue.is_empty():
            self.first_queue.add(self.second_queue.pop())

    def pop(self):
        """
        :rtype: int
        """
        while not self.second_queue.is_empty():
            self.first_queue.add(self.second_queue.pop())
        if not self.first_queue.is_empty():
            return self.first_queue.pop()

    def top(self):
        """
        :rtype: int
        """
        while not self.second_queue.is_empty():
            self.first_queue.add(self.second_queue.pop())
        if not self.first_queue.is_empty():
            return self.first_queue.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.first_queue.is_empty() and self.second_queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
