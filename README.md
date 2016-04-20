# Test Storm topology replay and logging

Apache Storm spout can be [reliable or unreliable](http://storm.apache.org/releases/current/Concepts.html). 
Developers must implement their own replay mechanism for the spout to act on tuple failure to make it reliable.
For example, if the upstream is a message queue, every time the spout read a message, it does not delete the message 
from the queue until the tuple has been processed and the spout is acked. This way, should the tuple fails, 
the spout can read the same message again from the queue and re-process it.

This project demonstates a simple replay mechanism with a simulated message queue as well as 
logging for each component to visualize the result.
