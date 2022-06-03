#sendin.py     by Orion Peter Fernandes - 65047854

from scapy.all import *

send(IP(src="172.20.10.1",dst="172.20.10.4")/TCP(dport=1024))
send(IP(src="172.20.10.2",dst="172.20.10.4")/TCP(dport=1025))
send(IP(src="172.20.10.3",dst="172.20.10.4")/TCP(dport=1026))
send(IP(src="172.20.10.4",dst="172.20.10.4")/TCP(dport=1027))
send(IP(src="172.20.10.5",dst="172.20.10.4")/TCP(dport=1028))
send(IP(src="172.20.10.6",dst="172.20.10.4")/TCP(dport=1029))
send(IP(src="172.20.10.7",dst="172.20.10.4")/TCP(dport=1030))
send(IP(src="172.20.10.8",dst="172.20.10.4")/TCP(dport=1031))
send(IP(src="172.20.10.9",dst="172.20.10.4")/TCP(dport=1032))
send(IP(src="172.20.10.10",dst="172.20.10.4")/TCP(dport=1033))


