import socket
import RemoteAPI_pb2  # the _pb2 suffix here has nothing to do with proto version, god knows why google named it this way lol
import serial
import time

DEBUG = True
PC_UDP_PORT = 6001

print("[INFO] Writing to serial interface \'/dev/ttyACM0\'")
print("[INFO] Since this script uses a UDP socket, it DOES NOT need to know the IP address of the sender. Instead, " + \
      "you should provide the IP address of your local interface that the socket should be listening to.")
PC_UDP_IP = input("Please Enter Local Interface IPv4 (e.g. 192.168.xx.xx): ")

ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 115200

cmd_sock = socket.socket(socket.AF_INET, # Internet
                  socket.SOCK_DGRAM) # UDP
cmd_sock.bind((PC_UDP_IP, PC_UDP_PORT))

cmd = RemoteAPI_pb2.Commands()

if DEBUG:
    print("[DEBUG] entering while loop")

while True:
    data, addr = cmd_sock.recvfrom(1024) # buffer size is 1024 bytes
    # cmd.ParseFromString(data)

    if DEBUG:
        print("[DEBUG] successful receive from UDP socket")
        print("[DEBUG] writing to serial")

    bytes_written = ser.write(data)

    if DEBUG:
        print("[DEBUG] bytes written: %d", bytes_written)

    data2 = ser.readline()

    if DEBUG:
        print("[DEBUG] successful read from serial")

    data2 = data2.rstrip()

    if DEBUG:
        print("[DEBUG] strip done")

    cmd.ParseFromString(data2)
    print("<x, y, z>: [%f, %f, %f]", cmd.motion_set_point.x, cmd.motion_set_point.y, cmd.motion_set_point.z)
