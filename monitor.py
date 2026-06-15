import socket, time, random

SERVER_IP = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        client.connect((SERVER_IP, PORT))
        print("[Patient Monitor] Connected to server")
        break
    except ConnectionRefusedError:
        print("[Patient Monitor] Server not ready, retrying in 3s...")
        time.sleep(3)

while True:
    bp = random.randint(110, 140)
    spo2 = random.randint(90, 100)
    msg = f"PatientMonitor: BP={bp}, SpO2={spo2}%"
    client.send(msg.encode())
    print(f"[Patient Monitor] Sent: {msg}")
    time.sleep(6)
