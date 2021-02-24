import socket
from main_Movement import movement


def init():
    #CREATES SOCKET
    connecting = True
    HOST = '192.168.20.126' #+ input("Host: 192.168.20.")
    #HOST = '172.16.4.' + input("Host: 192.168.21.")
    PORT = 4242
    while connecting:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST,PORT))
            print("Binded %s:%s" % (HOST,PORT))
            client_socket.sendall(b'motor client')
            connecting = False
            return client_socket
        except:
            print("failed to connect")
def main():
    sock = init()
    connected = True
    while connected:
        input = sock.recv(4092)
        data = input.decode()
        if data != "esc":
            movement(data)
        else:
            sock.close()
            connected = False
main()
