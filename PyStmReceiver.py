# import RemoteAPI_pb2
import serial, os

DEBUG = True

'''
Connect USB cable from RPi to RM board
'lsusb' terminal command lists Bus & Device
'ls -l /dev/serial* lists /dev/serial*
'''
ser = serial.Serial('/dev/ttyACM0')
# ser = serial.Serial('/dev/serial1')
ser.baudrate = 115200
# cmd = RemoteAPI_pb2.Commands()

if ser.isOpen():
    try:
        while ( True ):
            print("Serial port is open")
            reading = bytes((input() + '\n'), "UTF-8")
            print(str(reading))
            ser.write(reading)
            print("Wrote successfully")
            print(ser.readline().decode("UTF-8"))
    finally:
        ser.close()

# if DEBUG:
#     print("[DEBUG] entering while loop")

# while True:
#     data = ser.readline()

#     if DEBUG:
#         print("[DEBUG] successful read from serial")

#     data = data.rstrip()
#     print(data.decode())

    # # cmd.ParseFromString(data)
    # print("<x, y, z>: [%f, %f, %f]", cmd.motion_set_point.x, cmd.motion_set_point.y, cmd.motion_set_point.z)