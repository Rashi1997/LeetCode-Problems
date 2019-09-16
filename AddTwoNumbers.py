# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class BruteForce:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead=ListNode(0);
        carry=0;
        p=l1;
        q=l2;
        curr=dummyHead;
        while(p!=None or q!=None):
            if(p!=None): x=p.val;
            else:x=0;
            if(q!=None): y=q.val;
            else:y=0;
            summ=carry+x+y;
            carry=int(summ/10);
            curr.next=ListNode(summ %10);
            curr=curr.next;
            if(p!=None): p=p.next;
            if(q!=None): q=q.next;
        if(carry>0):
            curr.next=ListNode(carry);
        return dummyHead.next;
        
class Recursion:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
