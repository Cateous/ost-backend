from flask import Flask, request, jsonify
import sys
from pathlib import Path
import os

# Allow importing from project root
sys.path.append(str(Path(__file__).resolve().parents[1]))

from ost.core.scan import run_nmap
from ost.core.dir_brute import bruteforce
from ost.core.payloads import generate_reverse_shells
from ost.core.recon import subdomain_enum
from ost.core.whois_lookup import lookup

app = Flask(__name__)

@app.route('/')
def home():
    return '🔥 Offensive Security Toolkit API is running!'

# 1. Nmap Scan
@app.route('/scan', methods=['POST'])
def scan_route():
    data = request.get_json()
    target = data.get('target')
    flags = data.get('flags', [])
    if not target:
        return jsonify({'error': 'Target not provided'}), 400

    result = run_nmap(target, flags)
    return jsonify({'nmap_result': result})

# 2. Directory Brute Force
@app.route('/dirbrute', methods=['POST'])
def dirbrute_route():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL not provided'}), 400

    result = bruteforce(url)
    return jsonify({'dir_brute_result': result})

# 3. Reverse Shell Generator
@app.route('/generate-payload', methods=['POST'])
def generate_payload_route():
    data = request.get_json()
    ip = data.get('ip')
    port = data.get('port')
    if not ip or not port:
        return jsonify({'error': 'IP and Port required'}), 400

    result = generate_reverse_shells(ip, port)
    return jsonify({'payloads': result})

# 4. Subdomain Enumeration
@app.route('/subdomain', methods=['POST'])
def subdomain_route():
    data = request.get_json()
    domain = data.get('domain')
    if not domain:
        return jsonify({'error': 'Domain not provided'}), 400

    result = subdomain_enum(domain)
    return jsonify({'subdomains': result})

# 5. WHOIS + IP Lookup
@app.route('/whois', methods=['POST'])
def whois_route():
    data = request.get_json()
    domain = data.get('domain')
    if not domain:
        return jsonify({'error': 'Domain not provided'}), 400

    result = lookup(domain)
    return jsonify({'whois_info': result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
