# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None
            tempList = []
            while head:
                tempList.append(head.val)
                head = head.next
            temp=tempList[::-1]
            print(temp)
            
            nodeList = [ListNode() for _ in temp] #store nodes here
            newHead=ListNode()
            for i, node in enumerate(nodeList):
                nodeList[i].val = temp[i]
                if i+1 > (len(temp) - 1):
                    nodeList[i].next = None
                else:
                    nodeList[i].next = nodeList[i+1]


            return nodeList[0]
            



