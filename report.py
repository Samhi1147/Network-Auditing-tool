import json
import csv
from datetime import datetime
import os

def save_report(host, alive, open_ports, recommendations):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "host": host,
        "alive": alive,
        "open_ports": open_ports,
        "recommendations": recommendations,
        "timestamp": timestamp
    }

    with open("reports/scan_report.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("reports/scan_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Host", "Alive", "Open Ports", "Recommendations", "Timestamp"])
        writer.writerow([host, alive, open_ports, recommendations, timestamp])
