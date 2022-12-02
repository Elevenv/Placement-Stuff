# https://leetcode.com/problems/sort-list/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
            
        l.sort()
        
        root = temp = ListNode(0)
  
        # i = 0
        # while i<len(l):
        #     temp.next = ListNode(l[i])
        #     # temp.val = l[i]
        #     temp = temp.next
        #     i+=1
        # return root.next
        curr = head
        for i in l:
            curr.val = i
            curr = curr.next
            
        return head