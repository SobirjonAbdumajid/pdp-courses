class Queue:
    def __init__(self):
        self.queue = []
    
    def enque(self, items):
        self.queue.append(items)
    
    def deque(self, index):
        return self.queue[index]
    
    def size(self):
        return len(self.queue)
queue1 = Queue()
queue1.enque('Sobirjon')
queue1.enque('Sardorbek')
print(queue1.size())
# queue1.queue[0] = 'Sardorbek'
print(queue1.deque(0))
print(queue1.deque(1))
