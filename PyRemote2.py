import RemoteAPI_pb2 # the _pb2 suffix here has nothing to do with proto version, god knows why google named it this way lol
import socket
import time

TritonBot_IP = "127.0.0.1"
vision_port = 6003

vision_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
vision_socket.bind((TritonBot_IP, vision_port))
while True:
    data, addr = vision_socket.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    read_vision_data = RemoteAPI_pb2.VisionData()
    parsed_data = read_vision_data.ParseFromString(data)
    print(parsed_data)