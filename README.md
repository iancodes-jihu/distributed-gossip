# Distributed Gossip System

## What is this

a Gossip protocol or epidemic protocol is a procedure or process of computer peer to peer communication that is based on the way epidemics spread. in these python mock up system i stimulated 3 nodes to do the gossip protocoll that could do:
- Gossip push protocol: Fast, peer-to-peer message propagation over TCP sockets
- Anti-Entropy pull repair. periodic backgroudn threads (start_pulling) waking up every 2 seconds to compare seen message and heal dropped packets

## How to run
to run this project you can just go to terminal :

1. chose expriment you want try
2. write in terminal that file name using this format "python -m foldername.filename"
3. observe how diffrent condition change how to epidemic spread

in order to call the node.py inside the src function that you wanna called

## What im observve 
what i observer is that when new message arive its getting send to the peers and if the message is already seen its getting ignore. 

Push-only limit: when network drops occur, push-only gossip fails to reach 100% convergence

Anti-Entropy pull victory: backgorund pull reconculliation heals dropped messages within 1-2 seconds, achieving 100% eventual consistency!

## Experiment Results
you can see the Experiment Results in the folder docs, result_table.md



