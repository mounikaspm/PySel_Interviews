class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()

    def peek(self):  # peeks or returns last item in the list which is to be removes or just last item/next item
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


obj = Queue()
obj.enqueue('APPLE')
obj.enqueue(20)
obj.enqueue('THEN ORANGE')
print(obj.items)
obj.dequeue()
print(obj.items)
print(obj.peek())
print(obj.size())
print(obj.is_empty())
