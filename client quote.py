import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.0.2.5", 8888))

quote = client.recv(1024).decode()
print("Today’s quote: ", quote)

client.close()
