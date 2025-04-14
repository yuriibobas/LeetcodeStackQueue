""" Maximum Frequency Stack """

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


class FreqStack(object):
    """ Frequency Stack """
    def __init__(self):
        self.stack = Stack()
        self.frequencies = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.push(val)
        if val not in self.frequencies:
            self.frequencies[val] = 1
        else:
            self.frequencies[val] += 1

    def pop(self):
        """
        :rtype: int
        """
        most_frequency = max(self.frequencies.values())
        additional_stack = Stack()
        while True:
            if self.frequencies[self.stack.peek()] == most_frequency:
                result =  self.stack.pop()
                while not additional_stack.is_empty():
                    self.stack.push(additional_stack.pop())
                return result
            additional_stack.push(self.stack.pop())


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
