from ost.utils.helpers import log_output
import requests

def subdomain_enum(domain):
    print(f"\n[+] Enumerating subdomains for {domain}")
    subdomains = ["www", "mail", "ftp", "test", "dev", "admin"]
    found = []

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=2)
            if res.status_code < 400:
                result = f"[+] Found: {url} ({res.status_code})"
                print(result)
                found.append(result)
        except requests.RequestException:
            continue

    if found:
        log_output("\n".join(found), "subdomain_results.txt")
        return found
    else:
        print("[-] No valid subdomains found.")
        return ["No valid subdomains found."]
