#Benchmark plan

Goal:
Measure how long it takes for a gossip message to reach all alive nodes.

Start Condition:
nodeA.handle_message(msg)

Finish Condition:
All alive nodes contain msg.id in seen_messages

Measurement Tool:
time.perf_counter()

Nodes:
nodeA
nodeB
nodeC

Current Scenario:
nodeB.alive = False

Expected Result:
nodeA and nodeC receive the message.

