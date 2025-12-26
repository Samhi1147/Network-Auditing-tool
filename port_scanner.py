import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

def scan_ports(host):
    open_ports = []
    for port, service in COMMON_PORTS.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append((port, service))
            s.close()
        except:
            pass
    return open_ports
