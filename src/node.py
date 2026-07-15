import socket
import json
import uuid
import threading
import time
import random
from time import perf_counter

HOST = "127.0.0.1"
PORT_A= 5001
PORT_B= 5002
PORT_C= 5003

PEERS_A = [5002, 5003]
PEERS_B = [5001, 5003]
PEERS_C = [5001, 5002]

class message:
    def __init__(self, id, origin, payload):
        self.id = id
        self.origin = origin
        self.payload = payload

    def to_dict(self):
        return{
            "id": str(self.id),
            "origin": self.origin,
            "payload": self.payload
        }

    
class Node:


    def __init__(self, id, neighbors, port ):
        self.id = id
        self.neighbors = neighbors
        self.port = port
        self.alive = True
        self.seen_messages = set()
        self.packet_drop_rate =0.0
        # handle, check if message is new, add to seen set, and forward to peers
    def handle_message(self, msg):
        if self.alive == False:
            return
        else:
                if msg.id in self.seen_messages:
                    print("Node", self.id, "ignore msg", msg.id, "already seen")
                    return
                elif random.random() < self.packet_drop_rate :
                    print("sharks is biting the cable...")
                    return
                else:
                        self.seen_messages.add(msg.id)
                        self.forward_message(msg)
        #send new message to connect and send it to all peers
    def send_message(self,  msg, peer_port): 
            with socket.socket(socket.AF_INET ,socket.SOCK_STREAM)as s:
                s.connect((HOST, peer_port))
                s.sendall(json.dumps(msg.to_dict()).encode())
            print("Node", self.id, "sending msg", msg.id)
            return
    

#forward-ing message to the peers
    def forward_message(self, msg):
        
        for peer_port in self.neighbors: #huh we already had this
            self.send_message(msg, peer_port)
            print("Node", self.id, "forward msg", msg.id, "to", peer_port)


#listenin and waiting if there's a new message on loop    
    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
                    s.bind((HOST, self.port))
                    s.listen()
                    while True:
                        conn, addr = s.accept()
                        with conn: 
                            print(f"connected with {addr}")
                            data = conn.recv(1024)
                            if not data:
                                break
                            raw = data.decode()
                            data_dict = json.loads(raw)
                            incoming_msg = message(id=str(data_dict["id"]), origin=data_dict["origin"], payload=data_dict["payload"])
                            self.handle_message(incoming_msg)

def benchmark(nodes, msg, initiator_node):
    start = time.perf_counter()
    initiator_node.handle_message(msg)
    
    while not all(msg.id in node.seen_messages for node in nodes if node.alive):
        print("message havent been seen, still waiting for he messege to be send...")
        time.sleep(0.1)
    # What should we do inside the loop while waiting?

    end = time.perf_counter()
    elapsed_time = end - start
    print(f"Convergence completed in {elapsed_time:.4f} seconds.")

    return elapsed_time





if __name__ == "__main__":
    msg = message (
    id = str(uuid.uuid4()),
    origin = "A",
    payload = "Hello from A"
    )

    nodeA = Node(id="5001", neighbors=PEERS_A, port= PORT_A)
    nodeB = Node(id="5002", neighbors=PEERS_B, port= PORT_B)
    nodeC = Node(id="5003", neighbors=PEERS_C, port= PORT_C)

    nodes = [nodeA,nodeB,nodeC]

    thread_a = threading.Thread(target=nodeA.listen)
    thread_b = threading.Thread(target=nodeB.listen)
    thread_c = threading.Thread(target=nodeC.listen)
    thread_a.start()
    thread_b.start()
    thread_c.start()
    time.sleep(1)

    print(benchmark(nodes = [nodeA,nodeB,nodeC], msg=msg, initiator_node=nodeC))









#Given:
#The benchmark has started.


#nodeB.alive = False
#print(benchmark(nodes=[nodeA, nodeB, nodeC], msg=msg)) 
                            
                    
                       
#Then:
#It can inspect those nodes.         

    



#Benchmark Workflow
#1. Record start time.
#2. Start gossip.
#3. Repeatedly check every alive node.
#4. Stop when every alive node has msg.id.
#5. Record finish time.
#6. Compute elapsed time.
#7. Print the result.

