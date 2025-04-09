""" Implement Queue using Stacks """

class Stack:
    """ Stack """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class MyQueue(object):
    """ My Queue """
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while not self.second_stack.is_empty():
            self.first_stack.push(self.second_stack.pop())
        self.first_stack.push(x)

    def pop(self):
        """
        :rtype: int
        """
        while not self.first_stack.is_empty():
            self.second_stack.push(self.first_stack.pop())
        if not self.second_stack.is_empty():
            return self.second_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        while not self.first_stack.is_empty():
            self.second_stack.push(self.first_stack.pop())
        if not self.second_stack.is_empty():
            return self.second_stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.first_stack.is_empty() and self.second_stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
