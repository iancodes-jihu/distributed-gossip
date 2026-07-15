import socket
import json
import uuid
import threading
import time
from time import perf_counter
from src.node import Node, benchmark, message

HOST = "127.0.0.1"
PORT_A= 5001
PORT_B= 5002
PORT_C= 5003

PEERS_A = [5002, 5003]
PEERS_B = [5001, 5003]
PEERS_C = [5001, 5002]


if __name__ == "__main__":
    msg = message (
    id = str(uuid.uuid4()),
    origin = "A",
    payload = "Hello from A"
    )

    nodeA = Node(id="5001", neighbors=PEERS_A, port= PORT_A)
    nodeB = Node(id="5002", neighbors=PEERS_B, port= PORT_B)
    nodeC = Node(id="5003", neighbors=PEERS_C, port= PORT_C)
    nodeA.alive = False
    nodeB.alive = False
    nodeC.alive = False
    nodes = [nodeA,nodeB,nodeC]

    thread_a = threading.Thread(target=nodeA.listen)
    thread_b = threading.Thread(target=nodeB.listen)
    thread_c = threading.Thread(target=nodeC.listen)
    thread_a.start()
    thread_b.start()
    thread_c.start()
    time.sleep(1)

    print(benchmark(nodes = [nodeA,nodeB,nodeC], msg=msg, initiator_node=nodeA))
    print(nodeA.seen_messages)
    print(nodeB.seen_messages)
    print(nodeC.seen_messages)

