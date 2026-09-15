import selectors
import socket

HOST = "127.0.0.1"
PORT = 10450


def accept_wrapper(sock):
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, data=addr)


    def broadcast(message, sender_sock):
    for key in sel.get_map().values():
        sock = key.fileobj
        if sock != server and sock != sender_sock:
        try:
            sock.sendall(message)
        except:
            pass


    def service_connection(key, mask):
    sock = key.fileobj
    addr = key.data
    data = sock.recv(1024)
    if data:
        print(f"Received from {addr}: {data.decode().strip()}")
        broadcast(b"Broadcast: " + data, sock)
    else:
        print(f"Closing connection to {addr}")
        sel.unregister(sock)
        sock.close()

def main()
    sel = selectors.DefaultSelector()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    server.setblocking(False)
    sel.register(server, selectors.EVENT_READ, data=None)

    print(f"Listening on {HOST}:{PORT}")


    while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
        accept_wrapper(key.fileobj)
        else:
        service_connection(key, mask)

if __name__ == "__main__":
    main()