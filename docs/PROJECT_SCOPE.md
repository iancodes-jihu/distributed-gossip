i build this project to answer the few of question that i had about disstributed system 

such of this one
When a node fails, what happens to the messages that were supposed to go through it? Does the network stop? Does it route around? This is the interesting question. Write what YOUR simulation will do specifically.

my answer before the expriement:
        my simulation will mark thats as failure. but when the agent a failed to give information to agent b. i could do a gossip protocol called pull. you see the first way ifnromation goes was by push-ing it to the nodes . but what happen when it failed?my porgram will do pull proctocol where now the agent b will ask the agent a what rumors does it have. i can then turn this into push and pull protocol to help me achieve as smooth runnoing network.