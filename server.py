import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

def handle_device(conn, addr):
    print(f"[+] Connected: {addr}")
    try:
        with open("patient_data.txt", "a") as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decoded = data.decode()
                print(f"[Server] Received: {decoded}")
                file.write(decoded + "\n")
    except Exception as e:
        print("[!] Error:", e)
    finally:
        conn.close()
        print(f"[-] Disconnected: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)
print(f"[+] Server listening on {HOST}:{PORT}")

while True:
    try:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_device, args=(conn, addr))
        thread.start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down")
        break
