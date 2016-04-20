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
            id = hash(msg)
            self.queue.append(id)
            self.tbl[id] = msg

    def next_msg(self):
        try:
            id = self.queue[0]
            return id, self.tbl[id]
        except IndexError:
            raise StopIteration('no messages left.')

    def delete_msg(self, id):
        del self.tbl[id]
        self.queue.remove(id)
