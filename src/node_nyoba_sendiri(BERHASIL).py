import socket
import json
import uuid
import threading
import time

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

    def to_dict(self):
        return{
            "id": str(self.id),
            "origin": self.origin,
            "payload": self.payload
        }

    
class Node:


    def __init__(self, id, neighbors, port):
        self.id = id
        self.neighbors = neighbors
        self.port = port
        self.pesan_sudah_dibaca = set()
        
    def handle_message(self, psn):
        if psn.id in self.pesan_sudah_dibaca:
            print("Node", self.id, "ignore psn", psn.id, "already seen")
            return
        else:
            self.pesan_sudah_dibaca.add(psn.id)
            self.foward_message(psn)

    def send_message(self,  psn, peer_port): 
            with socket.socket(socket.AF_INET ,socket.SOCK_STREAM)as s:
                s.connect((HOST, peer_port))
                s.sendall(json.dumps(psn.to_dict()).encode())
            print("Node", self.id, "mengirimkan psn", psn.id)
            return
    

#handle_message, self, print
    def foward_message(self, psn):
        
        for peer_port in self.neighbors:
            self.send_message(psn, peer_port)
            print("Node", self.id, "forward psn", psn.id, "to", peer_port)


    
    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
            s.bind((HOST, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn: 
                print(f"Di koneksikan oleh {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    raw = data.decode()
                    data_dict = json.loads(raw)
                    psn_baru = message(id=data_dict["id"], origin=data_dict["origin"], payload=data_dict["payload"])
                    self.handle_message(psn_baru)
                
psn = message (
    id = uuid.uuid4(),
    origin = "A",
    payload = "Hello from A"
)


nodeA = Node(id="5004", neighbors=PEERS_A, port= PORT_A)
nodeB = Node(id="5002", neighbors=PEERS_B, port= PORT_B)
nodeC = Node(id="5003", neighbors=PEERS_C, port= PORT_C)

thread_a = threading.Thread(target=nodeA.listen)
thread_b = threading.Thread(target=nodeB.listen)
thread_c = threading.Thread(target=nodeC.listen)
thread_a.start()
thread_b.start()
thread_c.start()
time.sleep(1)

nodeA.handle_message(psn)

