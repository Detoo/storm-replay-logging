from collections import deque


class MessageQueue(object):
    MESSAGES = [
        'message #1',
        'message #2'
    ]

    def __init__(self):
        self.queue = deque()
        self.tbl = dict()
        for msg in self.MESSAGES:
            id = str(hash(msg))
            self.queue.append(id)
            self.tbl[id] = msg

    def next_msg(self):
        try:
            id = self.queue.popleft()
            return id, self.tbl[id]
        except IndexError:
            raise StopIteration('no messages left.')

    def requeue_msg(self, id):
        if id in self.tbl:
            self.queue.appendleft(id)

    def delete_msg(self, id):
        del self.tbl[id]
