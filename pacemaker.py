import socket, time, random

SERVER_IP = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Retry connection until server is ready
while True:
    try:
        client.connect((SERVER_IP, PORT))
        print("[Pacemaker] Connected to server")
        break
    except ConnectionRefusedError:
        print("[Pacemaker] Server not ready, retrying in 3s...")
        time.sleep(3)

while True:
    heart_rate = random.randint(60, 100)
    msg = f"Pacemaker: HeartRate={heart_rate}"
    client.send(msg.encode())
    print(f"[Pacemaker] Sent: {msg}")
    time.sleep(5)
