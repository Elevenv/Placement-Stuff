# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    # def show(self):
    #     if self.head is None:
    #         print("Linked list is empty")  
    #         return
    #     itr = self.head
    #     llstr = ""
    #     while itr:
    #         llstr += str(itr.data) + ' => '
    #         itr = itr.next
    #     print(llstr)         
    
    def reverse(self):
        ll_reverse = ''
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        self.head = prev      
        
if __name__ == '__main__':

    l1 = LinkedList()    
    l2 = LinkedList()   
 
    for i in range(0,3):
        data = int(input())
        l1.insert(data)
    
    for i in range(0,3):
        data = int(input())
        l2.insert(data)  
    
    l1.reverse()
    l2.reverse()
    l1_str = ''
    l2_str = ''
    while l1.head != None:
        l1_str += str(l1.head.data)
        l1.head = l1.head.next    
        
    while l2.head != None:
        l2_str += str(l2.head.data)
        l2.head = l2.head.next
    
    print("Addtion of two linked list is : ",int(l1_str)+int(l2_str))