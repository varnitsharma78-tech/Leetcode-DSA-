# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        result = []
        counter = 0

        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        dummy = ListNode(0)
        current = dummy

        while heap:
            value = heapq.heappop(heap)
            current.next = ListNode(value)
            current = current.next

        return dummy.next

        