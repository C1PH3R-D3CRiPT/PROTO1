'''
Network practice-1 IN python
'''

import socket
import threading
import sys


class TCPclient():
    '''REciever end'''

    def __init__(self) -> None:
        self.nickname = input("Choose your nickname: ")
        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 60000))
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        write_thread = threading.Thread(target=self.write)
        write_thread.start()
        

        # Listening to Server and Sending Nickname
    def receive(self):
        '''reciever froms server'''
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except OSError:
                # Close Connection When Error
                print("An error occured!")
                self.client.close()
                break

    def write(self):
        '''write messages'''
        while True:
            message = '{}: {}'.format(self.nickname, input(''))
            self.client.send(message.encode('ascii'))
    
    


if '__main__' == __name__:
    TCPclientobject = TCPclient()
  
    try:
        TCPclientobject.receive()
    except KeyboardInterrupt:
        print(" Okay Byeeeee.......")
        sys.exit()
