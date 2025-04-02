import pyshark
from tqdm import tqdm

def list_all_ips(capture):
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
