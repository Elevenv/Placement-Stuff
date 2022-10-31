class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def Append(self,item):
        if self.last_node is None:
            self.head = Node(item)
            self.last_node = self.head
        else:
            self.last_node.next = Node(item)
            self.last_node = self.last_node.next
    def Delete(self,item):
        temp = self.head

        if temp is not None:
            self.head = temp.next
            temp = None
            return
        
        while temp is not None:
            if temp.data == item:
                break
            prev = temp 
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def Display(self):
        while self.head != None:
            print(self.head.item,end=' ')
            self.head = self.head.next
        return
if __name__=='__main__':
    ll = LinkedList()
    n = int(input('Enter n: '))
    for _ in range(n):
        item = int(input('Enter item: '))
        ll.Append(item)
    # ll.Display()
    ll.Delete(3)
    ll.Display()
    print('\n')


