

# sample rules
firewall_rules = [
    {"action": "ALLOW", "ip": "192.168.1.10", "port": 80, "protocol": "TCP"},
    {"action": "ALLOW", "ip": "10.0.0.5", "port": 22, "protocol": "TCP"},
    {"action": "DENY",  "ip": "0.0.0.0", "port": 0, "protocol": "ALL"},  # default deny
]


def evaluate_packet(packet):
    for rule in firewall_rules:
        if (
            (rule["ip"] == packet["ip"] or rule["ip"] == "0.0.0.0")
            and (rule["port"] == packet["port"] or rule["port"] == 0)
            and (rule["protocol"] == packet["protocol"] or rule["protocol"] == "ALL")
        ):
            return rule["action"]
    return "DENY"  # default to deny if no match


def main():
    print("=== Firewall Rule Simulator ===")
    ip = input("Enter packet source IP: ")
    port = int(input("Enter packet destination port: "))
    protocol = input("Enter protocol (TCP/UDP): ").upper()

    packet = {"ip": ip, "port": port, "protocol": protocol}
    action = evaluate_packet(packet)
    print(f"\n[RESULT] Packet from {ip}:{port} using {protocol} is: {action}")

if __name__ == "__main__":
    main()
