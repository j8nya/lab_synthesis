#   a->b->c
#   (((0*2)+a)*2+b)*2+c

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        #пока не конец списка 
        while head:
            res = 2 * res + head.val
            head = head.next
        return res
        
