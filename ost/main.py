import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from core import recon, scan, whois_lookup, dir_brute, payloads

def main():
    while True:
        print("\n" + "="*40)
        print("🛠️  Offensive Security Toolkit (OST)")
        print("="*40)
        print("1. Subdomain Enumeration")
        print("2. Port Scan (Nmap)")
        print("3. WHOIS + DNS Lookup")
        print("4. Directory Bruteforce")
        print("5. Reverse Shell Generator")
        print("0. Exit")
        print("="*40)

        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter domain: ")
            recon.subdomain_enum(target)

        elif choice == "2":
            target = input("Enter IP or domain: ")
            scan.run_nmap(target)

        elif choice == "3":
            target = input("Enter domain/IP: ")
            whois_lookup.lookup(target)

        elif choice == "4":
            url = input("Enter base URL (e.g. https://example.com/): ")
            dir_brute.bruteforce(url)

        elif choice == "5":
            payloads.generate()

        elif choice == "0":
            print("Exiting OST. Stay sharp, hacker 👋")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Exiting... (Interrupted by user)")
