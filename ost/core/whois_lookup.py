import whois
import socket
from ost.utils.helpers import log_output

def lookup(domain):
    output = f"\n[+] WHOIS info for {domain}\n"

    # WHOIS Lookup
    try:
        w = whois.whois(domain)
        whois_data = str(w)
        print(whois_data)
        output += whois_data + "\n"
    except Exception as e:
        error_msg = f"[!] WHOIS lookup failed: {e}"
        print(error_msg)
        output += error_msg + "\n"

    # IP Resolver
    output += f"\n[+] Resolving IP for {domain}\n"
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Resolved IP: {ip}")
        output += f"Resolved IP: {ip}\n"
    except Exception as e:
        error_msg = f"[!] DNS resolution failed: {e}"
        print(error_msg)
        output += error_msg + "\n"

    # Save to logs
    log_output(output.strip(), "whois_results.txt")
    return output.strip()
