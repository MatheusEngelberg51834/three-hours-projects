import threading
import socket
import time
from collections import defaultdict

host, port = '127.0.0.1', 3003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients_addres = defaultdict(str)

def broadcast(message):
    for client in clients_addres:
        client.send(message)

#refactor those buffer overflow attempts while loops
def handle(client):
    while True:
        time.sleep(1)
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            pass

def recieve():
    while True:
        time.sleep(1)
        client, address = server.accept()
        print(str(address), 'connected')

        clients_addres[client] += address[0]

        print(address[0], 'connected')
        broadcast(f'{address[0]} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

recieve()