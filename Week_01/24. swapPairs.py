# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
		# 递归的终止条件
	    if not (head and head.next):
		    return head

	    tmp = head.next

	    head.next = self.swapPairs(tmp.next)

	    tmp.next = head
	    return tmp

# 递归