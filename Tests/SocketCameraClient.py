import cv2
import socket
import struct
import pickle

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host_ip = '192.168.18.53'
port = 8485
client_socket.connect((host_ip, port))

# Open the webcam
cam = cv2.VideoCapture(0)

while True:

    # Read a frame from the webcam
    ret, frame = cam.read()

    # Serialize the frame
    data = pickle.dumps(frame)

    # Pack the serialized frame into a struct
    message = struct.pack('Q', len(data)) + data

    # Send the frame to the server
    client_socket.sendall(message)

    cv2.imshow('Client Side Streaming', frame)
    if cv2.waitKey(1) == 13:  # Press 'Enter' to stop streaming
        break

cam.release()
cv2.destroyAllWindows()
client_socket.close()
