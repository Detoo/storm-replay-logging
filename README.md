# Test Storm topology replay and logging

Apache Storm spout can be [reliable or unreliable](http://storm.apache.org/releases/current/Concepts.html). Developers must implement their own replay mechanism for the spout to act on tuple failure to make it reliable.

This project demonstates a simple replay mechanism for a reliable spout as well as logging for each component.
