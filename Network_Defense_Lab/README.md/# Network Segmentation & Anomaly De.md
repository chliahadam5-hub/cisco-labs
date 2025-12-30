**# Network Segmentation \& Anomaly Detection Lab**



**## 1. Project Overview**

**I designed a secure network architecture to simulate a corporate environment (Interns vs. Servers) and developed a custom Python tool to test traffic visibility.**



**\* \*\*Goal:\*\* Enforce East-West segmentation and detect unauthorized bot traffic.**

**\* \*\*Tech Stack:\*\* Cisco IOS (Packet Tracer), Python, Wireshark.**



**## 2. Network Architecture**

**\* \*\*Topology:\*\* Segmented LAN with Router-on-a-Stick.**

**\* \*\*Security Policy:\*\* ACL 101 applied inbound on G0/0 to block HTTP (TCP/80) while permitting ICMP.**

**\* \*\*Result:\*\* Interns can Ping servers (Business continuity) but cannot Web Browse (Risk mitigation).**



**!\[Network Topology](images/1\_network\_topology.png)**



**## 3. Evidence of Security**

**The ACL successfully filters traffic based on Layer 3/4 logic.**

**\* \*\*Blocked:\*\* HTTP Requests from PC0 to PC1 timed out.**

**\* \*\*Allowed:\*\* ICMP (Ping) packets passed successfully.**



**!\[ACL Matches Log](images/2\_router\_acl\_matches.png)**

**!\[Web Block Proof](images/3\_web\_block\_proof.png)**



**## 4. Traffic Automation \& Detection**

**Wrote a Python script (`http\_monitor\_v4.py`) to inject a custom "User-Agent" signature into web requests.**

**\* \*\*Detection:\*\* Intercepted the traffic with Wireshark and identified the bot signature.**



**!\[Bot Detection](images/4\_bot\_detection.png)**

