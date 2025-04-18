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

