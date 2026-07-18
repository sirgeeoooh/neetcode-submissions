# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            res = []
            for i in range(0,len(lists), 2):
                if i + 1 < len(lists):
                    res.append(self.merge_two(lists[i],lists[i+1]))
                else:
                    res.append(lists[i])
            lists = res
        return lists[0] if lists else None

    def merge_two(self,l1, l2):
        node = ListNode()
        cur = node
        l1 = l1
        l2 = l2

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        
        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2

        return node.next 

                