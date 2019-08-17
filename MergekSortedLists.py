class DivideAndConquer:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else ListNode(0).next

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        point.next=l1 or l2
        return head.next
        
class BruteForce:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        all_nums=[]
        for l in lists:
            while l:
                all_nums.append(l.val)
                l=l.next
        head=curr=ListNode(0)
        for i in sorted(all_nums):
            curr.next=ListNode(i)
            curr=curr.next
        return head.next
