import socket
import threading

nickname = input('choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 3003))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print('Error ocurred')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input()}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()