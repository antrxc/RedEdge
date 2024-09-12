import logging

class DecentralizedNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node_id):
        self.nodes.append(node_id)
        logging.info(f"Node {node_id} added to decentralized network")

    def broadcast_message(self, sender_id, message):
        logging.info(f"Broadcasting message from {sender_id}: {message}")
        for node in self.nodes:
            if node != sender_id:
                self.receive_message(node, message)

    def receive_message(self, receiver_id, message):
        logging.info(f"Node {receiver_id} received message: {message}")
