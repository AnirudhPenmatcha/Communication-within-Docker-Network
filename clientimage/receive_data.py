import socket
import hashlib
import subprocess


def receive_file_with_checksum(sock, file_path):
    """Receive file along with its checksum from the server."""
    try:
        # Receive file size
        size = int(sock.recv(1024).decode())
        sock.sendall(b'ACK')

        # Receive checksum
        checksum = sock.recv(1024).decode()
        sock.sendall(b'ACK')

        # Receive file data
        received_data = b''
        while len(received_data) < size:
            chunk = sock.recv(4096)
            if not chunk:
                break
            received_data += chunk

        # Write received data to file
        with open(file_path, 'wb') as f:
            f.write(received_data)

        # Verify checksum
        if hashlib.md5(received_data).hexdigest() == checksum:
            print("File received successfully and checksum verified.")
        else:
            print("Checksum verification failed.")

    except Exception as e:
        print("Error:", e)

def receive_file():
    # Server configuration
    host_address = '172.19.0.3'  # Server IP address
    port_number = 8888
    
    # File to save received data
    file_path = 'received_file.txt'

    # Create client socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        # Connect to server
        client_sock.connect((host_address, port_number))
        print(f"Connected to server at {host_address}:{port_number}")

        # Receive file with checksum from server
        receive_file_with_checksum(client_sock, file_path)


receive_file()
subprocess.call(['ping', '172.19.0.3'])
