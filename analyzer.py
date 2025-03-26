import pyshark

udp_packets = []

def network_conversation(packet):
  try:
    protocol = packet.transport_layer
    if (protocol == "UDP"):
      udp_packets.append(packet)
    source_address = packet.ip.src
    source_port = packet[packet.transport_layer].srcport
    destination_address = packet.ip.dst
    destination_port = packet[packet.transport_layer].dstport
    return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port}')
  except AttributeError as e:
    pass

capture = pyshark.FileCapture('capture.pcapng')
conversations = []
for packet in capture:
  results = network_conversation(packet)
  if results != None:
    conversations.append(results)

print("UDP PACKETS")
for packet in udp_packets:
  print(packet)