import pyshark

def transport_packets(file): 
    capture = pyshark.FileCapture(file)

    udp_packets = []
    tcp_packets = []

    for packet in capture:
        try:
            protocol = packet.transport_layer 
            if protocol == "UDP":
                udp_packets.append(packet)
            elif protocol == "TCP":
                tcp_packets.append(packet)
        except AttributeError:
            pass

    transport_packets_results = {
        "udp_count": len(udp_packets),
        "tcp_count": len(tcp_packets),
       # "udp_packets": udp_packets,
       # "tcp_packets": tcp_packets
    }

    return transport_packets_results
