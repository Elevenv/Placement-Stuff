# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        List1 = ''
        List2 = ''
        
        temp = l1
        while temp:
            List1+=str(temp.val)
            temp = temp.next
        
        temp2 = l2
        while temp2:
            List2+=str(temp2.val)
            temp2 = temp2.next
        List1 = List1[::-1]
        List2 = List2[::-1]
        ans = str(int(List1)+int(List2))[::-1]
        
        root = n = ListNode(0)
        i = 0
        while i<len(ans):
            n.next = ListNode(int(ans[i]))
            n = n.next
            i+=1
        return root.next


# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self,data):
#         if self.head is None:
#             self.head = Node(data,None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data,None)
    
#     # def show(self):
#     #     if self.head is None:
#     #         print("Linked list is empty")  
#     #         return
#     #     itr = self.head
#     #     llstr = ""
#     #     while itr:
#     #         llstr += str(itr.data) + ' => '
#     #         itr = itr.next
#     #     print(llstr)         
    
#     def reverse(self):
#         ll_reverse = ''
#         prev = None
#         current = self.head
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
            
#         self.head = prev      
        
# if __name__ == '__main__':

#     l1 = LinkedList()    
#     l2 = LinkedList()   
 
#     for i in range(0,3):
#         data = int(input())
#         l1.insert(data)
    
#     for i in range(0,3):
#         data = int(input())
#         l2.insert(data)  
    
#     l1.reverse()
#     l2.reverse()
#     l1_str = ''
#     l2_str = ''
#     while l1.head != None:
#         l1_str += str(l1.head.data)
#         l1.head = l1.head.next    
        
#     while l2.head != None:
#         l2_str += str(l2.head.data)
#         l2.head = l2.head.next
    
#     print("Addtion of two linked list is : ",int(l1_str)+int(l2_str))