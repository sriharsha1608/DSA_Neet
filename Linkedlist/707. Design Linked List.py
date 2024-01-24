class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None


class MyLinkedList:

    def __init__(self):
        self.left=ListNode(0)
        self.right=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left
        

    def get(self, index: int) -> int:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1

        if cur and cur!=self.right and index==0:
            return cur.val
        return -1


    def addAtHead(self, val: int) -> None:
        prv,cur=self.left,ListNode(val)
        nxt=self.left.next
        prv.next=cur
        cur.next=nxt
        cur.prev=prv
        nxt.prev=cur
        

    def addAtTail(self, val: int) -> None:
        prv,cur=self.right.prev,ListNode(val)
        nxt=self.right
        prv.next=cur
        cur.next=nxt
        cur.prev=prv
        nxt.prev=cur
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur=self.left.next
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur and index==0:
            prv,node,nxt=cur.prev,ListNode(val),cur
            prv.next=node
            nxt.prev=node
            node.prev=prv
            node.next=nxt
            
    def deleteAtIndex(self, index: int) -> None:
        cur=self.left.next
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur and cur != self.right and index==0:
            prv,nxt=cur.prev,cur.next
            prv.next=nxt
            nxt.prev=prv
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)