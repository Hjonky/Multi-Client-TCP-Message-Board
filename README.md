# Multi-Client-TCP-Message-Board

An asynchronous, non-blocking multi-client TCP server in Python using the selectors module.

## Features
* **Non-blocking I/O:** Uses OS-level I/O multiplexing instead of heavy threading.
* **Real-time Broadcasting:** Any message received from a client is instantly relayed to all other connected users.
