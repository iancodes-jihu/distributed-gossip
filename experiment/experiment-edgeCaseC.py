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

ori = {
    "A": 5001, 
    "B": 5002,
    "C": 5003
}


if __name__ == "__main__":
    msg = message (
    id = str(uuid.uuid4()),
    origin = "A",
    payload = "Hello from A"
    )

    nodeA = Node(id="A", neighbors=PEERS_A, port= PORT_A, origin_to_port=ori)
    nodeB = Node(id="B", neighbors=PEERS_B, port= PORT_B, origin_to_port=ori)
    nodeC = Node(id="C", neighbors=PEERS_C, port= PORT_C, origin_to_port=ori)
    #nodeC.packet_drop_rate = 1.0 forgot to turn this into a comment
    nodes = [nodeA,nodeB,nodeC]

    thread_a = threading.Thread(target=nodeA.listen, daemon=True)
    thread_b = threading.Thread(target=nodeB.listen, daemon=True)
    thread_c = threading.Thread(target=nodeC.listen, daemon=True)
    thread_a_background = threading.Thread(target=nodeA.start_pulling, daemon=True)
    thread_b_background = threading.Thread(target=nodeB.start_pulling, daemon=True)
    thread_c_background = threading.Thread(target=nodeC.start_pulling, daemon=True)
    thread_a.start()
    thread_b.start()
    thread_c.start()
    thread_a_background.start()
    thread_b_background.start()
    thread_c_background.start()
    nodeB.packet_drop_rate = 0.5
    time.sleep(1)

    print(benchmark(nodes = [nodeA,nodeB,nodeC], msg=msg, initiator_node=nodeA))
    print(nodeA.seen_messages)
    print(nodeB.seen_messages)
    print(nodeC.seen_messages)

