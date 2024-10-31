class Queue:
    def __init__(self):
        self.queue = []
    
    def enque(self, items):
        self.queue.append(items)
    
    def deque(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
queue1 = Queue()
queue1.enque('Sobirjon')
queue1.enque('Sardorbek')
assert queue1.size() == 2
# assert queue1.deque() == "Apple"
# queue1.queue[0] = 'Sardorbek'
assert queue1.deque() == 'Sardorbek'
assert queue1.deque() == 'Sobirjon'
