
import socket, time, random

SERVER_IP = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        client.connect((SERVER_IP, PORT))
        print("[Infusion Pump] Connected to server")
        break
    except ConnectionRefusedError:
        print("[Infusion Pump] Server not ready, retrying in 3s...")
        time.sleep(3)

while True:
    infusion_rate = random.uniform(0.5, 5.0)
    msg = f"InfusionPump: Rate={infusion_rate:.2f}ml/hr"
    client.send(msg.encode())
    print(f"[Infusion Pump] Sent: {msg}")
    time.sleep(7)
