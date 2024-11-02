Publish-Subscribe Examples in Python
This repository contains Python code examples demonstrating different patterns of the Publish-Subscribe (Pub-Sub) architectural pattern.

Contents
Simple Pub-Sub
Force Event by Request
1. Simple Pub-Sub
The simple_pub_sub.py file demonstrates a basic implementation of the Pub-Sub pattern. In this example, we have the following components:

Publisher: Responsible for publishing (sending) events to the subscribers.
Subscriber: Responsible for receiving and handling the events published by the publisher.
Event Manager: Responsible for managing the subscription and publication of events.
The example shows how the publisher can publish events, and the subscribers can receive and process those events.

Usage
Run the simple_pub_sub.py file:
python simple_pub_sub.py

The output will show the events being published and the subscribers receiving and handling them.
2. Force Event by Request
The force_event_by_request.py file demonstrates a variation of the Pub-Sub pattern where the subscriber can request the publisher to force an event.

In this example, we have the following components:

Publisher: Responsible for publishing (sending) events to the subscribers.
Subscriber: Responsible for receiving and handling the events published by the publisher, and also for requesting the publisher to force an event.
Event Manager: Responsible for managing the subscription and publication of events, as well as handling the force event requests.
The example shows how the subscriber can request the publisher to force an event, and the publisher will respond by publishing the requested event.

Usage
Run the force_event_by_request.py file:
python force_event_by_request.py

The output will show the events being published, the subscribers receiving and handling them, and the subscribers requesting the publisher to force an event.
Requirements
Python 3.x
License
This project is licensed under the MIT License.
