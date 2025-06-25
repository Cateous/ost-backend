import requests
from ost.utils.helpers import log_output

def bruteforce(base_url):
    print(f"\n[+] Starting directory brute-force on {base_url}")
    found = []

    try:
        with open("utils/wordlist.txt", "r") as f:
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
            return found  # ✅ return to Flask API
        else:
            print("[-] No valid directories found.")
            return ["No valid directories found."]

    except FileNotFoundError:
        print("[-] wordlist.txt not found.")
        return ["wordlist.txt not found."]
