from time import sleep
from pyleus.storm import Spout

from app.message_queue import MessageQueue


class ReliableSpout(Spout):
    OUTPUT_FIELDS = ['message']

    def initialize(self):
        self.msg_queue = MessageQueue()

    def next_tuple(self):
        try:
            id, msg = self.msg_queue.next_msg()
            self.log('emitting message: {}'.format(msg))
            self.emit([msg], tup_id=id)
        except StopIteration:
            sleep(10)
            pass

    def ack(self, tup_id):
        self.log('acked (msg ID: {})'.format(tup_id))
        self.msg_queue.delete_msg(tup_id)

    def fail(self, tup_id):
        self.log('failed (msg ID: {})'.format(tup_id))
        self.msg_queue.requeue_msg(tup_id)


if __name__ == '__main__':
    ReliableSpout().run()
