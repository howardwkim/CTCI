class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class QueueViaStack(object):
    def __init__(self):
        self.main = []
        self.helper = []

    def enqueue(self, data):
        self.main.append(Node(data))

    def dequeue(self):
        if not self.helper and not self.main:
            raise KeyError
        elif not self.helper:
            while self.main:
                self.helper.append(self.main.pop(0))
        return self.helper.pop(0)


queue = QueueViaStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
for node in queue.main:
    print node.data
print
queue.dequeue()
for node in queue.main:
    print node.data
print
for node in queue.helper:
    print node.data