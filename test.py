import socket
import threading
import time
import uuid

HOST = "127.0.0.1"
NODE_A = 5001
NODE_B = 5002
NODE_C = 5003

PEERS_A = NODE_B, NODE_C
PEERS_B = NODE_A, NODE_C
PEERS_C = NODE_A, NODE_B

seen_message = set()

class Message:
    def __init__(self):
        self.

class Node:
    def __init__(self):
        s