when a node receives a message:
1.  it will see if its already seen the messege or not, by chechking the message id
2   it will remember it by put in the id in the list. and then spread it
3.  if its already seen it, it will not forward the message
4.  and when there's message failure. it will ask the previous agent to foward their message pull
5.  the sytem will do the push-pull cycle to spread the information

we yse sockets because they are sinpler than http for direct node to node communication