# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headOne = list1
        headTwo = list2

        newHead = ListNode()
        tempNode = newHead

        while headOne and headTwo:
            if headOne.val <= headTwo.val:
                tempNode.next = headOne
                headOne = headOne.next
                tempNode = tempNode.next
            else:
                tempNode.next = headTwo
                headTwo = headTwo.next
                tempNode = tempNode.next
        
        if headOne:
            tempNode.next = headOne
        if headTwo:
            tempNode.next = headTwo
        
        return newHead.next
