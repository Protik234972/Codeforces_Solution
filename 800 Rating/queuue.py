from collections import deque


class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue (self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    self.buffer.pop()
  def front(self):
    return self.buffer[0]
  def is_empty(self):
    return len(self.buffer)==0

  def size(self):
    return len(self.buffer)
q = Queue()
q.enqueue(17)
q.enqueue(24)
q.enqueue(39)
q.enqueue(55)
while q.size()>1:
  q.enqueue (q.front ())
  q.dequeue ()
  q.dequeue ()
print (q.front())
    