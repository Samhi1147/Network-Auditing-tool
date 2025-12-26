from liveness import is_alive
from port_scanner import scan_ports
from recommendations import generate_recommendations
from report import save_report

# Main function to run the network security tool
def main():
    host = input("Enter IP or domain: ")
# Check if host is alive by connecting to one of the ports
    alive = is_alive(host)
    print("Host Alive:", alive)

    open_ports = scan_ports(host)
    print("Open Ports:", open_ports)

    recommendations = generate_recommendations(open_ports)
    print("Security Recommendations:")
    for r in recommendations:
        print("-", r)

    save_report(host, alive, open_ports, recommendations)
    print("Report saved successfully")

if __name__ == "__main__":
    main()
