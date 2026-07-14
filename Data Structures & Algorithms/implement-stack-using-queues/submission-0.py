class DDLLNode:
    def __init__(self, val=0, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.next = nxt

    def queue(self, tail):
        tail.prev.next = self
        self.next = tail
        self.prev = tail.prev
        tail.prev = self

    def dequeue(self, head):
        head.next = head.next.next
        head.next.prev = head

class MyStack:

    def __init__(self):
        self.head = DDLLNode()
        self.tail = DDLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def push(self, x: int) -> None:
        node = DDLLNode(x)
        node.queue(self.tail)
        self.count += 1
        for _ in range(self.count - 1):
            front_node = self.head.next
            front_node.dequeue(self.head)
            front_node.queue(self.tail)
            
    def pop(self) -> int:
        node = self.head.next
        node.dequeue(self.head)
        self.count -= 1
        return node.val
        
    def top(self) -> int:
        node = self.head.next
        return node.val

    def empty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()