# https://leetcode.com/problems/reverse-linked-list/

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def Insert(self,item):
        if self.last_node is None:
            self.head = Node(item)
            self.last_node = self.head
        else:
            self.last_node.next = Node(item)
            self.last_node = self.last_node.next

    def DisplayLL(self):
        temp = self.head
        while temp:
            print(temp.item,end=' ')
            temp = temp.next
        return

    def ReverseLinkedList(self):
        prev,curr = None,self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        self.head = prev
        self.DisplayLL()

    def PrintReverse(self):
        add,ct = 0,0
        temp = self.head
        while temp:
            ct+=1
            add = temp
            temp = temp.next
        
        while ct:
            temp = self.head
            while add:
                print(temp.item)
                temp = temp.next
                add = temp
            ct-=1

if __name__=="__main__":
    ll = LinkedList()
    n = int(input("Enter no of elements : "))
    for _ in range(n):
        item = int(input("Enter item : "))
        ll.Insert(item)
    ll.DisplayLL()
    print('\n')
    ll.ReverseLinkedList()
    print('\n')
    ll.PrintReverse()
