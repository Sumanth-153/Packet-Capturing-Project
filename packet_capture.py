# packet_capture.py
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("=== Packet Capturing Started ===")
    print("Press Ctrl + C to stop capturing.\n")
    sniff(prn=packet_callback, store=False)  # store=False means it won't save in memory

if __name__ == "__main__":
    main()
  
