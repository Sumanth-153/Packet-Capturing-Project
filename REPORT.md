## 🧾 Packet Capturing Project Report


### 🧩 1. Introduction

Packet capturing is the process of intercepting and logging traffic that passes over a computer network.
It allows cybersecurity professionals and network administrators to monitor, analyze, 
and troubleshoot network issues by inspecting the data packets transmitted between devices. 
Tools like Scapy enable users to perform packet capture, filtering, and analysis
directly using Python programming.

### 🎯 2. Objective

The main objective of this project is to:

* Capture live network packets using Python.
* Understand how network packets are structured and transmitted.
* Build a simple and effective packet sniffer using the Scapy library.
* Demonstrate the importance of packet capturing in cybersecurity and network monitoring.

### ⚙ 3. Tools Used

| Tool               | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| Python             | Programming language used to write the packet sniffer script |
| Scapy              | Library for packet capturing and network analysis            |
| VS Code / Terminal | Used to write and execute the Python script                  |
| Operating System   | Windows / Linux (tested on both)                             |


### 🧠 4. Procedure

1. Install Python on your system (if not already installed).
2. Install Scapy using the command:

   bash
   pip install scapy
   
3. Create the Python script named packet_capture.py:

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
   
4. Run the script

   * On Windows (as Administrator):

     bash
     python packet_capture.py
     
   * On Linux:

     bash
     sudo python3 packet_capture.py
     
5. Observe live network packets displayed in the terminal.

### 💻 5. Code Explanation

* *from scapy.all import sniff* → Imports the sniff function used to capture packets.
* *packet_callback(packet)* → A callback function that runs every time a packet is captured.
* *packet.summary()* → Prints a short summary of the captured packet (protocol, source, destination).
* *sniff(prn=packet_callback, store=False)* → Starts capturing packets and calls packet_callback() for each one.
* *store=False* → Ensures packets are not stored in memory (saves RAM).

### 📊 6. Output Screenshots

Example output:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e8df9786-abd4-4051-8b3b-e34be75e68db" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/19c1cf39-6fb1-4683-b454-f02bb760a653" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d1ac5922-81cf-4188-822e-e1764b095217" />

Packet Capturing Started
Press Ctrl + C to stop capturing.

Ether / IP / TCP 192.168.1.3:56457 > 142.250.206.10:https PA / Raw
Ether / IP / TCP 192.168.1.3:56457 > 142.250.206.10:https A / Raw
Ether / IP / TCP 142.250.206.10:https > 192.168.1.3:56457 A
Ether / IP / TCP 192.168.1.3:56457 > 142.250.206.10:https A / Raw
Ether / IP / TCP 192.168.1.3:56457 > 142.250.206.10:https A / Raw
Ether / IP / TCP 142.250.206.10:https > 192.168.1.3:56457 A
Ether / IP / TCP 192.168.1.3:56457 > 142.250.206.10:https A / Raw
Ether / IP / UDP 142.250.77.138:https > 192.168.1.3:59997 / Raw

These lines show:

* Source and destination IPs
* Protocols (TCP, UDP, ARP)
* Live traffic summaries

### 🧩 7. Conclusion

This project successfully demonstrated how to capture and analyze live network packets using Python 
and Scapy. The implementation helped in understanding real-time data flow within a network and the structure 
of network packets. Packet capturing is a crucial skill for cybersecurity analysts, network engineers,
and ethical hackers for diagnosing issues and detecting malicious activities.
