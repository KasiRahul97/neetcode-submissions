"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        on={}
        curr=head
        while curr:
            copy=Node(curr.val)
            on[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=on[curr]
            copy.next=on.get(curr.next)
            copy.random=on.get(curr.random)
            curr=curr.next
        return on[head]