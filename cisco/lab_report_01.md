# Lab Report: Basic Network Segmentation & Routing
**Date:** 2025-12-22
**Status:** Success

## 1. Architecture
**Topology:**
![Topology](cisco-labs/Capture d'écran 2025-12-17 091749.png)

**IP Plan:**
- **Network A:** 192.168.10.0/24 (Left Side)
- **Network B:** 192.168.20.0/24 (Right Side)
- **Router Interfaces:** g0/0 (10.1), g0/1 (20.1)

## 2. Configuration & Verification
**Router Configuration:**
Commands used to bring up interfaces:
```bash
enable
configure terminal
interface g0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
interface g0/1
 ip address 192.168.20.1 255.255.255.0
 no shutdown