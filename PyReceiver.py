import socket
import RemoteAPI_pb2  # the _pb2 suffix here has nothing to do with proto version, god knows why google named it this way lol

PC_UDP_PORT = 6001

print("[INFO] Please check the IPv4 address of your PC. (It should not be 127.0.0.1)")
PC_UDP_IP = input("Please Enter Sender IPv4 (e.g. 127.0.0.1): ")


cmd_sock = socket.socket(socket.AF_INET, # Internet
                  socket.SOCK_DGRAM) # UDP
cmd_sock.bind((PC_UDP_IP, PC_UDP_PORT))

cmd = RemoteAPI_pb2.Commands()

while True:
    data, addr = cmd_sock.recvfrom(1024) # buffer size is 1024 bytes
    cmd.ParseFromString(data)
    print("<x, y, z>: [%f, %f, %f]", cmd.motion_set_point.x, cmd.motion_set_point.y, cmd.motion_set_point.z)

