import threading
import socket

host = '127.0.0.1' #Localhost
port = 7070


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove
            break 

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")


        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode('ascii')
        clients.append(client)

        print(f"Nickaname of the cliente is  {nickname}")
        broadcast(f"{nickname} join to the chat".encode('ascii'))

        client.send('Connected to the server!'.encode("ascii"))

        thread = threading.thread(target=handle, args=(client,))
        thread.start()
