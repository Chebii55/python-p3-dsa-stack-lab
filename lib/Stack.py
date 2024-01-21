class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items)==self.limit:
            return print("ERROR:Can't add because it is full!")
        else:
            self.items.append(item)

    def pop(self):
        if len(self.items)==0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items)!=self.limit:
            return False
        else:
            return True

    def search(self, target):
        if target in self.items:
            target_index=self.items.index(target)
            last_value=self.items[-1]
            how_far=self.items.index(last_value)-target_index
            return how_far
        else:
            return -1
stk = Stack([5,6,7,8,9,10])
print(stk.search(5)) #5
print(stk.search(8)) #2
print(stk.search(15)) #1