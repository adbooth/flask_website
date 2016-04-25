### ONESmart
---
ONESmart is a web application built for [Corning Inc.](http://www.corning.com/) designed to integrate with a proprietary proof of concept system for showcasing the speed of new networking technology.

The demonstration employs devices which only have network access through SMS, and the ONESmart program serves as an automated SMS streaming platform to communicate with these devices. ONESmart provides the system with a GUI rendered in HTML/CSS, which communicates via [websocket](http://socket.io/) with a backend built on the [Python](https://www.python.org/) [Flask](http://flask.pocoo.org/) webapp framework. The SMS data is sent via the [Twilio](https://www.twilio.com/) mobile communication API.
