from pyleus.storm import Bolt


class SlackBolt(Bolt):
    def initialize(self):
        self.slack_mode = False

    def process_tuple(self, tup):
        msg = tup.values[0]
        self.log('received message: {}'.format(msg))

        if self.slack_mode:
            self.log('uh oh, the bolt don\'t give a shit...')
        else:
            self.log('hard working and acking...')
            self.ack(tup)
            self.slack_mode = True  # alright, enough work


if __name__ == '__main__':
    SlackBolt().run()
