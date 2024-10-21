# The stack remains always ordered such that the highest value
# is at the top and the lowest at the bottom


class OrderedStack:
    def __init__(self):
        self.items = []

    def check_if_empty(self):
        return self.items == []

    def push_on_top(self, item):
        self.items.append(item)

    # push method to maintain order when pushing new elements
    def push(self, item):
        # This is a temp stack
        temp_stack: OrderedStack = OrderedStack()
        # Change > to < to inject fault
        if self.check_if_empty() or item > self.get_peek_item():
            self.push_on_top(item)
        else:
            while item < self.get_peek_item() and not self.check_if_empty():
                temp_stack.push_on_top(self.pop())
            self.push_on_top(item)
            while not temp_stack.check_if_empty():
                self.push_on_top(temp_stack.pop())

    def pop(self):
        if self.check_if_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def get_peek_item(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
