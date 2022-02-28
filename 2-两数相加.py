# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        ll = l3
        i=0
        while (l1 or l2 or i):
            if l2 and l1:
                res = l1.val+l2.val+i 
                l1, l2 = l1.next, l2.next
            elif l1:
                res = l1.val+i
                l1 = l1.next
            elif l2:
                res = l2.val+i
                l2 = l2.next
            else:
                res = i
            i, res = res // 10, res % 10
            l3.next = ListNode(res)
            l3 = l3.next
        return ll.next

l1 = ListNode(2); l1.next = ListNode(4); l1.next.next = ListNode(3)
l2 = ListNode(5); l2.next = ListNode(6); l2.next.next = ListNode(4)
res = Solution().addTwoNumbers(l1, l2)
while(res):
    print(res.val)
    res = res.next