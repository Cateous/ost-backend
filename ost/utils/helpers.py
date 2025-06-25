from datetime import datetime

def log_output(data, filename="output.txt"):
    with open(f"logs/{filename}", "a") as f:
        f.write(f"\n--- {datetime.now()} ---\n")
        f.write(data + "\n")
