import socket
import sys

def main():
    if len(sys.argv) != 3:
        print("Incorrect use of client.py")
        exit()
    
    # Parse the command line arguments
    server_addr = (sys.argv[1], int(sys.argv[2]))
    
    # Create a connection
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Communicate with the server
    while True:
        s.sendto(input().encode(), server_addr)

        data, _ = s.recvfrom(1024)
        print(data.decode())

if __name__ == '__main__':
    main()

