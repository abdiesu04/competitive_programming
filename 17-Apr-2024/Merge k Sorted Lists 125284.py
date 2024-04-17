# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ind,node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, ind,node))
        
        merged = ListNode()
        curr = merged
        
        while heap:
            val, ind , node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if curr.next:
                heapq.heappush(heap, (curr.next.val, ind, node.next))
            # print(heap)
        
        return merged.next