# Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import List, Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Define a helper function that merges two sorted linked lists
        def mergeTwoLists(l1, l2):
            # If one of the lists is empty, return the other list
            if not l1:
                return l2
            if not l2:
                return l1
            # Define a dummy node to serve as the head of the merged list
            dummy = ListNode(0)
            # Define a pointer for the merged list that starts at the dummy node
            curr = dummy
            # Traverse both lists and append the smaller node to the merged list
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            # Append the remaining nodes of the non-empty list to the merged list
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            # Return the merged list
            return dummy.next
        
        # Use a divide-and-conquer approach to merge all k lists
        if not lists:
            return None
        n = len(lists)
        # Merge pairs of adjacent lists until only one list remains
        while n > 1:
            new_lists = []
            # Merge each pair of adjacent lists
            for i in range(0, n, 2):
                if i + 1 < n:
                    new_lists.append(mergeTwoLists(lists[i], lists[i+1]))
                else:
                    new_lists.append(lists[i])
            lists = new_lists
            n = len(lists)
        # Return the final merged list
        return lists[0]


# The function first defines a helper function mergeTwoLists that merges two sorted linked lists 
# in ascending order. It does this by defining a dummy node that serves as the head of the merged 
# list, and traversing both input lists while appending the smaller node to the merged list. 
# Once one of the input lists is empty, it appends the remaining nodes of the non-empty list to 
# the merged list and returns it.
# The mergeKLists function uses a divide-and-conquer approach to merge all k lists. It first 
# checks if the input list is empty, and returns None if it is. It then repeatedly merges adjacent 
# pairs of lists until only one list remains. The merging is done by calling the mergeTwoLists 
# function on each pair of adjacent lists and appending the result to a new list. Once all pairs 
# have been merged, the function replaces the original list with the new list and repeats the process 
# until only one list remains. Finally, the function returns the final merged list.
# The given code defines a class Solution that contains a function mergeKLists that takes a list of k linked lists as input and returns a single sorted linked list as output.

# The linked list is defined using the ListNode class, which has two attributes val and next. 
# The val attribute stores the value of the current node, and the next attribute is a reference 
# to the next node in the linked list.
# The function mergeKLists takes a list of linked lists as input and first removes any empty linked
# lists from the list using a list comprehension. It then initializes an empty linked list called
# dummy and a pointer curr that points to the last node of the dummy linked list.
# The function then repeatedly finds the smallest value node among the heads of all 
# linked lists and appends it to the dummy linked list by updating the next attribute of the curr pointer. The next attribute of the node with the smallest value is then updated to point to the next node in its linked list. 
# This process continues until all linked lists are empty.
# Finally, the next attribute of the first node of the dummy linked list is returned as the head of 
# the merged linked list.