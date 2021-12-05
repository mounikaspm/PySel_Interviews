class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):  # item to be removed is not specified as, in list last item will be taken automatically
        if self.items:
            return self.items.pop()

    def next_item(self):  # peeks or returns last item in the list
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []  # simple check


'''
When a method runs 'indexing' into a list, it is done in a constant time O(1)
'''

obj1 = Stack()
obj1.push(10)
obj1.push(20)
obj1.pop()
print(obj1.next_item())
print(obj1.items)
print(obj1.size())
print(obj1.is_empty())
