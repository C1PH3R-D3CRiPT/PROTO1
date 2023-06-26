''' Creating a TCP chatbot in python'''
import socket
import threading
import sys

class TCPserver():
    '''Class for TCP server'''

    def __init__(self) -> None:
        self.host = '127.0.0.1'
        self.port = 60000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast_messages(self, message):
        '''Broad cast messages to client'''
        for client in self.clients:
            client.send(message)

    # Handling Messages From Clients

    def handle_the_clients(self, client):
        '''handling the clients done here'''
        while True:
            try:
                # broadcast_messagesing Messages
                message = client.recv(1024)
                self.broadcast_messages(message)
            except OSError:
                # Removing And Closing Clients
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast_messages(
                    '{} left!'.format(nickname).encode('ascii'))
                self.nicknames.remove(nickname)
                break

    # Receiving / Listening Function

    def receive(self):
        '''Recieve messages from the clients'''
        while True:
            # Accept Connection
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))

            # Request And Store Nicknamea
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            # Print And broadcast_messages Nickname
            print("Nickname is {}".format(nickname))
            self.broadcast_messages(
                "{} joined!".format(nickname).encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(
            target=self.handle_the_clients, args=(client,))
            thread.start()


if '__main__' == __name__:
    TCPserverobject = TCPserver()
    try:
        TCPserverobject.receive()
    except KeyboardInterrupt:
        print(" Okay Byeeeee.......")
        sys.exit()