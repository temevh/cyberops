import pyshark
cap = pyshark.FileCapture('capture.pcapng')
print(cap[0])