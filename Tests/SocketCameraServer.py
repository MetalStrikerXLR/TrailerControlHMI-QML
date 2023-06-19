import cv2
import socket
import struct
import pickle

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'
port = 8485

# Bind the socket to a specific IP and port
server_socket.bind((host_ip, port))

# Listen for incoming connections
server_socket.listen(5)

while True:
    print('Waiting for a new connection...')
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print('Connection from:', addr)

    # Receive and display the frames
    data = b''
    payload_size = struct.calcsize('Q')

    while True:
        # Receive the payload size
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # Adjust the buffer size as needed
            if not packet:
                break
            data += packet

        # Break the loop if no more data is received or if connection is closed
        if not packet:
            break

        # Unpack the payload size
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack('Q', packed_msg_size)[0]

        # Receive the frame data
        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)  # Adjust the buffer size as needed
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserialize the frame
        frame = pickle.loads(frame_data)

        # Display the frame
        cv2.imshow('Server Side Streaming', frame)

        if cv2.waitKey(1) == 13:  # Press 'Enter' to stop receiving frames
            break

    # Release resources
    cv2.destroyAllWindows()
    client_socket.close()

# Close the server socket
server_socket.close()