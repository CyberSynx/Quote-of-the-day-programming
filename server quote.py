import random
import socket
import threading

quotes = [
    "Positive anything is better than negative nothing.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Happiness is not something ready made. It comes from your own actions.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Don't watch the clock; do what it does. Keep going.",
    "Hardships often prepare ordinary people for an extraordinary destiny."
]

def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("10.0.2.5", 8888))
server.listen(5)

print("Quote of the Day server is listening… ")

while True:
    client, addr = server.accept()
    print("Received connection from: ", addr)
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
