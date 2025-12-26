def generate_recommendations(open_ports):
    recommendations = []

    for port, service in open_ports:
        if port == 21:
            recommendations.append("FTP is insecure, use SFTP instead")
        elif port == 22:
            recommendations.append("Secure SSH with key-based authentication")
        elif port == 80:
            recommendations.append("Use HTTPS instead of HTTP")
        elif port == 3306:
            recommendations.append("Do not expose database ports publicly")

    if not recommendations:
        recommendations.append("No major security risks detected")

    return recommendations
