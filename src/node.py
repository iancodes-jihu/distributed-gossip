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

ori = {
    "A": 5001,
    "B": 5002,
    "C": 5003
    }

class message:
    def __init__(self, id, origin, payload, msg_type = "gossip" ):
        self.id = id
        self.origin = origin
        self.payload = payload
        self.msg_type = msg_type

    def to_dict(self):
        return{
            "id": str(self.id),
            "origin": self.origin,
            "payload": self.payload,
            "msg_type": self.msg_type
        }

    
class Node:


    def __init__(self, id, neighbors, port, origin_to_port):
        self.id = id
        self.neighbors = neighbors
        self.port = port
        self.alive = True
        self.seen_messages = set()
        self.packet_drop_rate =0.0
        self.message_db = {}#equivalent to all_assigment
        self.origin_to_port = origin_to_port



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
                        self.message_db[msg.id] = msg
                        self.seen_messages.add(msg.id)
                        self.forward_message(msg)
        #send new message to connect and send it to all peers

    def handle_pull_request(self, msg):
        if self.alive == False:
            return
        else:
                    for msg_id, message in self.message_db.items():
                        if msg_id not in msg.payload:
                            print("Node", self.id, "deosnt have the", msg_id, "sending the missing message",)
                            resolved_address = self.origin_to_port[msg.origin]
                            self.send_message(message, resolved_address)
                        else:
                            print("Node", self.id, "ignore msg", msg_id)
                    return


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
                            incoming_msg = message(id=str(data_dict["id"]), origin=data_dict["origin"], payload=data_dict["payload"], msg_type=data_dict["msg_type"])
                            if incoming_msg.msg_type == "pull_request":
                                self.handle_pull_request(incoming_msg)
                            else:
                                self.handle_message(incoming_msg)

    def pull_loop(self):
        while self.alive:
            time.sleep(2)
            target_peer = random.choice(self.neighbors)
            seen_list = list(self.seen_messages)
            msg_pull_loop = message(
                id=str(uuid.uuid4()),
                origin= self.id,
                payload= seen_list,
                msg_type="pull_request"
            )
            self.send_message(msg_pull_loop, target_peer)

    def start_pulling(self):
        card = self.pull_loop
        worker = threading.Thread(target=card)
        worker.start()




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
    payload = "Hello from A",
    #msg_type = "pull_request"
    )

    nodeA = Node(id="A", neighbors=PEERS_A, port= PORT_A, origin_to_port=ori)
    nodeB = Node(id="B", neighbors=PEERS_B, port= PORT_B, origin_to_port=ori)
    nodeC = Node(id="C", neighbors=PEERS_C, port= PORT_C, origin_to_port=ori)

    nodes = [nodeA,nodeB,nodeC]

    thread_a = threading.Thread(target=nodeA.listen)
    thread_b = threading.Thread(target=nodeB.listen)
    thread_c = threading.Thread(target=nodeC.listen)
    thread_a_background = threading.Thread(target=nodeA.start_pulling)
    thread_b_background = threading.Thread(target=nodeB.start_pulling)
    thread_c_background = threading.Thread(target=nodeC.start_pulling)
    thread_a.start()
    thread_b.start()
    thread_c.start()
    thread_a_background.start()
    thread_b_background.start()
    thread_c_background.start()
    time.sleep(1)

    print(benchmark(nodes = [nodeA,nodeB,nodeC], msg=msg, initiator_node=nodeA))









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

