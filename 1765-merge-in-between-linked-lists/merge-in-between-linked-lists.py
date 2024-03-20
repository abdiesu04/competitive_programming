# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize two pointers to the head of list1
        prev_node_of_sublist = curr_node = list1

        # Move prev_node_of_sublist to the node just before position 'a'
        for _ in range(a - 1):
            prev_node_of_sublist = prev_node_of_sublist.next
      
        # Move curr_node to the node at position 'b'
        for _ in range(b):
            curr_node = curr_node.next
      
        # Connect the node before 'a' with the head of list2
        prev_node_of_sublist.next = list2
      
        # Traverse to the end of list2 to find the last node
        while prev_node_of_sublist.next:
            prev_node_of_sublist = prev_node_of_sublist.next
      
        # Connect the last node of list2 with the node after 'b' in list1
        prev_node_of_sublist.next = curr_node.next
      
        # The node at position 'b' no longer has any references and can be collected by garbage collector

        # Return the merged list starting with list1's head
        return list1