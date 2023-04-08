# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified 
# list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of # # # nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
from typing import List, Optional, ListNode
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize the dummy node and pointers for reversing
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while True:
            # Initialize pointers for each group
            start = prev.next
            end = prev
            
            # Check if there are k nodes remaining to reverse
            for i in range(k):
                end = end.next
                if not end:
                    return dummy.next
            
            # Reverse the group of k nodes
            next_group = end.next
            curr = start
            prev_node = next_group
            
            while curr != next_group:
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp
            
            # Reconnect the reversed group to the original list
            prev.next = end
            start.next = next_group
            prev = start

# First, we define the reverse function that takes a start and an end node as input. 
# This function reverses the links between the nodes in the linked list from start to end. 
# We use the standard technique of maintaining three pointers: prev, curr, and next to traverse 
# the linked list and reverse the links.
# In the reverseKGroup function, we first calculate the length of the linked list by traversing it once. 
# Then, we use a dummy node dummy as the head of the resulting linked list and initialize it to point 
# to the original head of the linked list.
# We also initialize prev and tail to point to the dummy node. The prev pointer will keep track of the 
# last node of the previous group, while the tail pointer will keep track of the last node of the 
# current group.
# We use a loop to process the linked list in groups of size k. Inside the loop, we check if there
# are at least k nodes left in the linked list. If not, we break out of the loop since there are no
#  more groups to reverse.
# If there are k or more nodes left, we use two nested loops to reverse the nodes in the current group. 
# The inner loop calls the reverse function to reverse the links between the nodes in the group. 
# We update the prev and tail pointers to point to the last node of the previous group and the 
# last node of the current group, respectively.
# Finally, we connect the reversed group to the previous group by updating the links between 
# the prev node and the first node of the reversed group, and between the last node of the 
# reversed group and the next node after the group.
# After the loop finishes, we return the dummy.next node, which is the head of the resulting 
# linked list.

