What you simulated — nodeB marked as dead
What you observed — nodeB received messages but did not forward them
What the network did — 5004 and 5003 continued communicating without 5002
What the limitation is — other nodes still try to send to dead nodes, they just get silently dropped

i simulated node failure using the atribute self.alive that i added in the beginning. at first it was confusing how to mark it. but turnout i need to go in handle funcation and add it there. what i observerd there when the nodeB marked as dead it still receive a message but its instanly dropped it. one things worth note is that the other peers doesnt exactly know that the peers is dead so they continnue to send the message until its realise its dead much in the reallife. the limitation is clearly its cannot dirrentiante the state between it was dead or not so it just get silently dropped

Limitation Analysis

# Current Limitations

1. Benchmark code not implemented yet
2. Only tested on a single machine
3. Node are threads, not separate machines
4. No network latency stimulation
5. small network size (3 nodes)

## Edge Cases & Failures Discovered.

1. How does the benchmark behave when the initiator is dead?
>immedietly goes to infinte loop of waiting because all the other node is alive. but the intiator is dead.but handle.message has no way of knowing that. making the infinite loop

2. How does the benchmark behave when all nodes are dead?
> Convergence immedietly reach, because well all the node are dead so it reach to the sama conclution. and its print the empty set of each node
3. How does the benchmark behave when a cable is cut (100% packet loss to one node)?
> when node C is experienxing packet lose. the other node still send its message to it. but because they have noway of knowing that the that. it goes to infinite loop waiting for the message to arrive. it also print sharks bite the cable as a way to comunitcate that the cable is cut



