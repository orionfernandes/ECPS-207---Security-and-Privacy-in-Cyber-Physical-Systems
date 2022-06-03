Using the Scapy (Links to an external site.) package, write two Python programs, a sending program and a receiving program. The sending program will send packets to your machine's IP address but to different ports, while spoofing different source IP addresses. The receiving program will sniff all the packets sent by the first program and print their summary to the screen.

Please note that the sending program must execute on a different machine from the receiving program. In order to accomplish this, you should either use two machines of your own, or you should execute your program on the machine of someone else who you know.  This is not a group project, but you can borrow someone else's machine in order to get your results. The second machine can also be a Raspberry Pi. If you have difficulty finding a second machine to execute your code on, please let the professor know so that he can help you find a solution.

Your sending program should send 10 TCP packets to your machine. Each packet should be sent to a different port number on your machine from port 1024 to port 1033. Each packet should have a different source IP address. Each source IP address should share the same high 3 bytes as the address of your machine, but it should use low byte values from 1 to 10.

Your receiving program should sniff all packets received by your machine and employ a filter to screen out only packets sent by your sending program. Specifically, the receiving program should use a filter to receive only packets whose source IP addresses and destination port numbers are in the ranges which are used by your sending program. Once sniffing is done, your receiving program should print the following information for each packet: source IP, destination IP, source port, destination port.