"""
ARES Message Broker
Centralized internal routing for tactical messages between modules.
"""
import logging

class MessageBroker:
    def __init__(self):
        self.subscribers = {} # {topic: [callback_functions]}
        logging.info("ARES Message Broker Initialized")

    def subscribe(self, topic, callback):
        """Subscribes a module to a specific tactical topic."""
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)
        logging.debug(f"Subscribed to {topic}")

    def publish(self, topic, message):
        """Publishes a message to all interested modules."""
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                try:
                    callback(message)
                except Exception as e:
                    logging.error(f"Error in subscriber callback for {topic}: {e}")

# Global instance for easy access across modules
broker = MessageBroker()
