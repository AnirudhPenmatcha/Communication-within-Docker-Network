import socket
import hashlib
import subprocess

def calculate_checksum(file_path):
    """Calculate checksum of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def send_file_with_checksum(client_sock, file_path):
    """Send file along with its checksum to the client."""
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Calculate checksum
        checksum = calculate_checksum(file_path)

        # Send file size and checksum
        client_sock.sendall(str(len(file_data)).encode())
        client_sock.recv(1024)  # Wait for acknowledgment
        client_sock.sendall(checksum.encode())
        client_sock.recv(1024)  # Wait for acknowledgment

        # Send file data
        client_sock.sendall(file_data)
        print("File sent successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

def main():
    # Server configuration
    host_address = '172.19.0.3'
    port_number = 8888
    file_path = 'random_data.txt'  # Path to the file to be sent

    # Create server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host_address, port_number))
        server_socket.listen(1)
        print(f"Server listening on {host_address}:{port_number}")

        while True:
            # Accept incoming connections
            client_socket, client_addr = server_socket.accept()
            print(f"Connected to client: {client_addr}")

            # Send file with checksum to the client
            send_file_with_checksum(client_socket, file_path)

            # Close connection
            client_socket.close()

if __name__ == "__main__":
    main()
    #subprocess.call(['ping', '172.19.0.2'])