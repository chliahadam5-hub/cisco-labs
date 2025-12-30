import requests
import time
from datetime import datetime

# Targets: Real sites to create real traffic
TARGETS = ["http://httpbin.org/get", "http://example.com"]

print("[*] Starting Twen-Security-Bot...")
print("[*] Press Ctrl+C to stop.\n")

try:
    while True:
        for url in TARGETS:
            try:
                # HEADER TRICK: We name ourselves "Twen-Security-Bot"
                # This is the breadcrumb we will find in Wireshark
                headers = {'User-Agent': 'Twen-Security-Bot/1.0'}
                
                start = time.time()
                r = requests.get(url, headers=headers, timeout=5)
                latency = round((time.time() - start) * 1000)
                
                status = "ONLINE" if r.status_code == 200 else f"ERR {r.status_code}"
                t = datetime.now().strftime("%H:%M:%S")
                print(f"[{t}] {status} | {latency}ms | {url}")
            except Exception as e:
                print(f"[!] FAIL: {url} - {e}")
        
        time.sleep(3) # Wait 3 seconds
except KeyboardInterrupt:
    print("\n[*] Stopped.")