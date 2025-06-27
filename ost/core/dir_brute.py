import os
import requests
from ost.utils.helpers import log_output

def bruteforce(base_url):
    print(f"\n[+] Starting directory brute-force on {base_url}")
    found = []

    # Ensure logs/ directory exists
    os.makedirs("logs", exist_ok=True)

    # Dynamically resolve absolute path to wordlist.txt
    wordlist_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  # goes from /core/ to /ost/
        "utils",
        "wordlist.txt"
    )

    # Debug: print actual path being accessed
    print(f"[DEBUG] Loading wordlist from: {wordlist_path}")

    try:
        with open(wordlist_path, "r") as f:
            paths = f.read().splitlines()

        for path in paths:
            url = f"{base_url.rstrip('/')}/{path}"
            try:
                res = requests.get(url, timeout=2)
                if res.status_code < 400:
                    result = f"[+] Found: {url} ({res.status_code})"
                    print(result)
                    found.append(result)
            except requests.RequestException:
                continue  # skip unreachable paths

        if found:
            log_output("\n".join(found), "dir_brute_results.txt")
            return found
        else:
            print("[-] No valid directories found.")
            return ["No valid directories found."]

    except FileNotFoundError:
        print(f"[-] wordlist.txt not found at: {wordlist_path}")
        return [f"wordlist.txt not found at: {wordlist_path}"]
