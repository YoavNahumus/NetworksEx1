import socket
import sys

# Adds an entry of domain to ip to the file
def add_entry(file_name, domain, ip):
    with open(file_name, 'a') as file:
        file.write("\n" + domain + "," + ip)

def main():
    if len(sys.argv) != 5:
        print("Incorrect use of server.py")
        exit()

    # Parse the command line arguments
    port = int(sys.argv[1])
    parnet_addr = (sys.argv[2], int(sys.argv[3]))
    file_name = sys.argv[4]

    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(('', port))

    ips = {}

    # Create the dictionary of domain names to ips
    with open(file_name, 'r') as file:
        lines = file.readlines() 
        for line in lines: 
            key, value = line.strip().split(',') 
            ips[key] = value

    # Receive data from the client
    while True:
        data, addr = s.recvfrom(1024)
        strdata = data.decode()
        if strdata in ips:
            s.sendto(ips[strdata].encode(), addr)
        else:
            # If data not in ips check in parent server
            s.sendto(data, parnet_addr)
            parent_data, _ = s.recvfrom(1024)
            ips[strdata] = parent_data.decode()
            add_entry(file_name, strdata, parent_data.decode())
            s.sendto(parent_data, addr)

if __name__ == '__main__':
    main()


