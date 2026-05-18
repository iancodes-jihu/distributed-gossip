import socket
import json
import uuid
import threading

HOST = "127.0.0.1"
PORT_A= 5004
PORT_B= 5002
PORT_C= 5003

PEERS_A = [5002, 5003]
PEERS_B = [5004, 5003]
PEERS_C = [5004, 5002]





seen_messages = set()

class message:
    def __init__(self, id, origin, payload):
        self.id = id
        self.origin = origin
        self.payload = payload
        


class Node:


    def __init__(self, id, neighbors):
        self.id = id
        self.neighbors = neighbors
        self.pesan_sudah_dibaca = set()
        
    def handle_message(self, psn):
        if psn.id in self.pesan_sudah_dibaca:
            print("Node", self.id, "ignore psn", psn.id, "already seen")
            return
        else:
            self.pesan_sudah_dibaca.add(psn.id)
            self.foward_message(psn)

    def send_message(self,  psn):
        log("Node", id, "received psn", psn.id)

        foward_message(psn)

    def foward_message(self, psn):
        for neighbor in neighbor:
            send_message(psn, neighbor)
            log("Node", id, "forward psn", psn.id, "to", neighbor,id)

psn = Message (
    id = generate__message_id(),
    origin = "A"
    payload = "Hello from A"
)

nodeA.handle_message(psn)


nodeA = Node(id="5004", neighbors=PEERS_A)
nodeB = Node(id="5002", neighbors=PEERS_B)
nodeC = Node(id="5003", neighbors=PEERS_C)