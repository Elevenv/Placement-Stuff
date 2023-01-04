class Queue:
    def __init__(self):
        self.queue = []
        self.maxSize = 3
    
    def enqueue(self,item):
        if len(self.queue)<self.maxSize:
            self.queue.append(item)
        else:
            print('Queue is full ')
    
    def dequeue(self):
        if len(self.queue)==0:
            print('Queue is empty')
        else:
            ele = self.queue[0]
            self.queue.pop(0)
            print(ele,' removed')

    def display(self):
        print(self.queue)

    def Length(self):
        print(len(self.queue))

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

# q.display()
# q.dequeue()
q.display()
q.Length()

del q