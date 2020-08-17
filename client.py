import  socket
import threading

PORT = 5050
HEADER = 64 # message length
FORMAT = 'UTF-8'
DISCONNECTED_MESSAGE = '!DISCONNECTED'

SERVER = socket.gethostbyname(socket.gethostname()) # getting the server automaically
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
	message = msg.encode(FORMAT)
	message_length = len(message)
	send_length = str(message_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))

send_message('Hello World!')