import RemoteAPI_pb2 # the _pb2 suffix here has nothing to do with proto version, god knows why google named it this way lol
import socket
import time
from pynput import keyboard

TritonBot_IP = "127.0.0.1"
RemoteCONN_Port = 6000
RemoteCMD_Port = 6001
GVisionServer_Port = 6003
# ...

def on_press(key):
    try:
        #print(type(key))
        if not (type(key) is keyboard.Key):
            if key.char == 'w':
                cmd.motion_set_point.y = pwr
            if key.char == 's':
                cmd.motion_set_point.y = -pwr
            if key.char == 'a':
                cmd.motion_set_point.x = -pwr
            if key.char == 'd':
                cmd.motion_set_point.x = pwr
            if key.char == 'q':
                cmd.motion_set_point.z = r_pwr
            if key.char == 'e':
                cmd.motion_set_point.z = -r_pwr
            if key.char == 'j':
                cmd.kicker_set_point.y = kick_z_force_small
                cmd.kicker_set_point.x = kick_force_small
            if key.char == 'k':
                cmd.kicker_set_point.y = kick_z_force
                cmd.kicker_set_point.x = kick_force
            # if key.char == 'p':
            #     cmd.enable_ball_auto_capture = True


    except AttributeError:
        # print('special key {0} pressed'.format(key))
        pass

def on_release(key):
    if not (type(key) is keyboard.Key):
        if key.char == 'w':
            cmd.motion_set_point.y = 0
        if key.char == 's':
            cmd.motion_set_point.y = 0
        if key.char == 'a':
            cmd.motion_set_point.x = 0
        if key.char == 'd':
            cmd.motion_set_point.x = 0
        if key.char == 'q':
            cmd.motion_set_point.z = 0
        if key.char == 'e':
            cmd.motion_set_point.z = 0
        if key.char == 'j':
            cmd.kicker_set_point.y = 0
            cmd.kicker_set_point.x = 0
        if key.char == 'k':
            cmd.kicker_set_point.y = 0
            cmd.kicker_set_point.x = 0
        # if key.char == 'p':
        #     cmd.enable_ball_auto_capture = False

    # ....


cmd = RemoteAPI_pb2.Commands()
cmd.enable_ball_auto_capture = False
cmd.mode = 3
cmd.is_world_frame = False
cmd.motion_set_point.x, cmd.motion_set_point.y, cmd.motion_set_point.z = 0.0, 0.0, 0.0
cmd.kicker_set_point.x, cmd.kicker_set_point.y = 0, 0

visData = RemoteAPI_pb2.VisionData()
visData.bot_pos.x = 0.0
visData.bot_pos.y = 0.0
visData.ball_pos.x = 0.0
visData.ball_pos.y = 0.0

cmd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
vision_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pwr = 80
r_pwr = 15
kick_z_force = 3
kick_force = 5
kick_z_force_small = 0
kick_force_small = 3

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    # print(visData)
    print("<", cmd.motion_set_point.x, ", ",
               cmd.motion_set_point.y, ", ",
               cmd.motion_set_point.z, ">")
    cmd_socket.sendto(cmd.SerializeToString(), (TritonBot_IP, RemoteCMD_Port))
    vision_socket.sendto(visData.SerializeToString(), (TritonBot_IP, GVisionServer_Port))

