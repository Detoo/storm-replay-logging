from time import sleep
from pyleus.storm import Spout

from app.messages import MESSAGES


class UnreliableSpout(Spout):
    OUTPUT_FIELDS = ['message']

    def initialize(self):
        self.msgs = iter(MESSAGES)

    def next_tuple(self):
        try:
            msg = next(self.msgs)
            self.log('emitting message: {}'.format(msg))
            self.emit([msg], tup_id=hash(msg))
        except StopIteration:
            sleep(10)
            pass

    def ack(self, tup_id):
        self.log('acked')

    def fail(self, tup_id):
        self.log('failed, meh')


if __name__ == '__main__':
    UnreliableSpout().run()
