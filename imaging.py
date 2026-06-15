import socket, time, random

SERVER_IP = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        client.connect((SERVER_IP, PORT))
        print("[Imaging] Connected to server")
        break
    except ConnectionRefusedError:
        print("[Imaging] Server not ready, retrying in 3s...")
        time.sleep(3)

while True:
    scan_type = random.choice(["CT", "MRI", "X-ray"])
    file_size = random.randint(100, 500)
    msg = f"Imaging: Type={scan_type}, Size={file_size}MB"
    client.send(msg.encode())
    print(f"[Imaging] Sent: {msg}")
    time.sleep(10)
