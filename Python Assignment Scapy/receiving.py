import random
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range
host = "172.20.10.1/10"
port_range = [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033]

# Send SYN with random Src Port for each Dst port
for dst_port in port_range:
    src_port = random.randint(1025,65534)
    resp = sr1(
        IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0,
    )

    if resp is None:
        print(f"{host}:{dst_port} is filtered (silently dropped)")

    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            # Send a gratuitous RST to close the connection
            send_rst = sr(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                timeout=1,
                verbose=0,
            )
            print(f"{host}:{dst_port} is open")

        elif (resp.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port}  is closed")
     
 #   For ICMP port scanning    
 #       elif(resp.haslayer(ICMP)):
 #       if(
 #           int(resp.getlayer(ICMP).type) == 3 and
 #           int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
 #       ):
 #
 # print(f"{host}:{dst_port} is filtered (silently dropped).")


