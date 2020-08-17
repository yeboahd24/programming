import  socket
import threading

PORT = 5050
HEADER = 64 # message length
FORMAT = 'UTF-8'
DISCONNECTED_MESSAGE = '!DISCONNECTED'

SERVER = socket.gethostbyname(socket.gethostname()) # getting the server automaically
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(addr, conn):
	'''Getting information from the client'''
	print(f"[NEW CONNECTIONS] {addr} connected.")

	connected = True
	while connected:
		msg_length = conn.recv(HEDAER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECTED_MESSAGE:
				connected = False

			print(f"[{addr}] {msg}")
			conn.send("Message recieved".encode(FORMAT))
	conn.close()


def start():
	server.listen()
	print(f"[LISTENING] Server is listenig on {SERVER}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
print("[STARTING] server is starting...")
start()

