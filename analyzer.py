import pyshark
from tqdm import tqdm

def transport_packets(capture): 
    udp_packets = []
    tcp_packets = []

    with tqdm(desc="Processing Packets", unit="pkt", dynamic_ncols=True) as pbar:
        for packet in capture:
            try:
                protocol = packet.transport_layer 
                if protocol == "UDP":
                    udp_packets.append(packet)
                elif protocol == "TCP":
                    tcp_packets.append(packet)
            except AttributeError:
                pass

            pbar.update(1)

    transport_packets_results = {
        "udp_count": len(udp_packets),
        "tcp_count": len(tcp_packets)
    }

    return transport_packets_results

def ip_list(capture):
    ip_addresses = set()

    with tqdm(desc="Gathering IP's", unit="IP", dynamic_ncols=True) as pbar:
        for packet in capture:
            try:
                if hasattr(packet, "ip"):
                    ip_addresses.add(packet.ip.src)
                    ip_addresses.add(packet.ip.dst)
            except AttributeError:
                pass
            pbar.update(1)
    input(f"found {len(ip_addresses)} different IP addresses")

    return list(ip_addresses)
