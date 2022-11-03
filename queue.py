maxSize = 4

class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        if len(self.queue)<maxSize:
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

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()
q.dequeue()
q.display()