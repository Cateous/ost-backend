import subprocess
from ost.utils.helpers import log_output

def run_nmap(target):
    print(f"\n[+] Running Nmap scan on {target}")

    print("\nChoose scan options by typing the flags (space-separated):")
    print("1. -sV  : Service/version detection")
    print("2. -F   : Fast scan (fewer ports)")
    print("3. -Pn  : Treat all hosts as online (skip ping)")
    print("4. -O   : OS detection")
    print("5. -sS  : TCP SYN scan (stealth)")
    print("6. -sT  : TCP connect scan")
    print("7. -A   : Aggressive scan (OS, version, script, traceroute)")
    print("8. -p-  : Scan all 65535 ports")
    print("9. -T4  : Faster execution (timing template)")
    print("10. -n  : Skip DNS resolution")
    print("Example: -sV -T4 -p-")

    flags_input = input("Enter Nmap flags (or press Enter for default -sV): ").strip()
    flags = flags_input.split() if flags_input else ["-sV"]

    try:
        result = subprocess.run(
            ["nmap", *flags, target],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        if output:
            log_output(output, "nmap_results.txt")
            return output
        else:
            return "No output received from Nmap."

    except Exception as e:
        return f"Error running Nmap: {e}"
