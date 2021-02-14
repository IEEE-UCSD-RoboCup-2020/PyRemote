import RemoteAPI_pb2
import serial

DEBUG = True

ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 115200
cmd = RemoteAPI_pb2.Commands()

if DEBUG:
    print("[DEBUG] entering while loop")

while True:
    data = ser.readline()

    if DEBUG:
        print("[DEBUG] successful read from serial")

    data = data.rstrip()

    cmd.ParseFromString(data)
    print("<x, y, z>: [%f, %f, %f]", cmd.motion_set_point.x, cmd.motion_set_point.y, cmd.motion_set_point.z)