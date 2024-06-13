from scapy.all import *

protoDict = {1: "ICMP", 4: "IP", 6: "TCP", 17: "UDP",
             21: "ftp", 22: "ssh", 23: "telnet", 80: "http"}
requestMethodSet = {"GET", "POST", "HEAD", "PUT", "PATCH", "DELETE"}


def is_request(d):
    request_method = d.split()[0]
    return request_method in requestMethodSet


def get_request_method(d):
    return d.split()[0]


def get_response_status(d):
    return int(d.split()[1])


# pkts = sniff(iface="MediaTek Wi-Fi 6 MT7921 Wireless LAN Card",
#              filter="host 192.168.180.47",
#              count=70)
#
# wrpcap("temp1.pcap", pkts)

pkts = rdpcap("temp1.pcap")

print("查看被捕获到的网络数据包的源IP地址、目的IP地址、源端口号、目的端口号以及具体的网络协议")
tplt = "{:^18}\t{:^18}\t{:^10}\t{:^10}\t{:^10}"
print(tplt.format("src", "dst", "sport", "dport", "proto"))
for pkt in pkts:
    try:
        if IP in pkt and TCP in pkt:
            print(tplt.format(pkt[IP].src, pkt[IP].dst, pkt[TCP].sport, pkt[TCP].dport, protoDict[pkt[IP].proto]))
    except Exception as e:
        print(e)

for pkt in pkts:
    try:
        if TCP not in pkt:
            continue
        if pkt[TCP].sport != 80 and pkt[TCP].dport != 80:
            continue

        data = str(bytes(pkt[TCP].payload))
        if len(data) < 4:
            continue

        data = data[2:-1]
        if is_request(data) == True:
            print("HTTP请求信息：")
            print("    request_method: %s" % get_request_method(data))
            print("    具体内容：%s" % data)
            continue

        if data[0:5] != "HTTP/":
            continue
        response_status = get_response_status(data)
        if 200 <= response_status < 600:
            print("HTTP应答信息：")
            print("    response_status: %s" % response_status)
            print("    具体内容：%s" % data)
    except Exception as e:
        print(e)
