What you simulated — nodeB marked as dead
What you observed — nodeB received messages but did not forward them
What the network did — 5004 and 5003 continued communicating without 5002
What the limitation is — other nodes still try to send to dead nodes, they just get silently dropped

i simulated node failure using the atribute self.alive that i added in the beginning. at first it was confusing how to mark it. but turnout i need to go in handle funcation and add it there. what i observerd there when the nodeB marked as dead it still receive a message but its instanly dropped it. one things worth note is that the other peers doesnt exactly know that the peers is dead so they continnue to send the message until its realise its dead much in the reallife. the limitation is clearly its cannot dirrentiante the state between it was dead or not so it just get silently dropped