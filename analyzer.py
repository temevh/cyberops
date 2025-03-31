import pyshark

def transport_packets(capture): 
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
        "tcp_count": len(tcp_packets)
    }

    return transport_packets_results

def ip_list(capture):
    ip_addresses = set()

    for packet in capture:
        try:
            if hasattr(packet, "ip"):
                ip_addresses.add(packet.ip.src)
                ip_addresses.add(packet.ip.dst)
        except AttributeError:
            pass

    return list(ip_addresses)
