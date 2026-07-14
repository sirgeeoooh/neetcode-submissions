class DDLLNode:
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.next = nxt

    def dequeue(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def queue(self, end):
        self.prev = end.prev
        self.prev.next = self
        self.next = end
        end.prev = self


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        front = DDLLNode(0)
        end = DDLLNode(0)
        front.next = end
        end.prev = front
        res = len(students)

        for _ in students:
            node = DDLLNode(_)
            node.queue(end)
        
        count = 0
        

        while sandwiches and count < res:  
            cur_node = front.next
            if cur_node.val == sandwiches[0]:
                cur_node.dequeue()
                res -= 1
                sandwiches.pop(0)
                count = 0
            else:
                cur_node.dequeue()
                cur_node.queue(end)
                count += 1

        return res

                    