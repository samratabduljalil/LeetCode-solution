# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or all(l is None for l in lists):
            return None
        heap  =[]
        for i , l in enumerate(lists):
            if l:
                heappush(heap, (l.val,i,l))
        dummy = ListNode()
        current = dummy
        while heap:
            val,i,node=heappop(heap)
            current.next=node
            current=current.next
            if node.next:
                heappush(heap,(node.next.val, i , node.next))
        return dummy.next                 