import os
import subprocess
from datetime import datetime
from sys import platform

# Log file for detected threats

Log_File = "C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\logs\\detected_threats.log"

#Function to log detected threats
def log_threats(ip_address, threat_type):
    os.makedirs(os.path.dirname(Log_File),exist_ok=True)
    with open(Log_File,"a") as log_file:
        log_file.write(f"[{datetime.now}] - Threat Detected:{threat_type} from IP:{ip_address}\n")
    print(f"Logged threat from IP:{ip_address}")



# function to block malicios  IPs

def block_ip(ip_address):
    try:
        if platform.system() == "Linux":
            # Linux: Block using iptables
            subprocess.run(["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"], check=True)
        elif platform.system() == "Windows":
            # Windows: Block using PowerShell
            subprocess.run(
                ["powershell",
                 "New-NetFirewallRule",
                 "-DisplayName",
                 f"Block_{ip_address}",
                 "-Direction", "Inbound",
                 "-RemoteAddress",
                 ip_address,
                 "-Action",
                 "Block"],
                check=True)
        print(f" Blocked IP: {ip_address}")
    except Exception as e:
        print(f" Failed to block IP {ip_address}: {e}")



def prevent_threat(ip_address, threat_type="Malicious Traffic"):
    log_threats(ip_address, threat_type)
    block_ip(ip_address)
