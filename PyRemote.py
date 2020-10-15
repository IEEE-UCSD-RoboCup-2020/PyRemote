import RemoteAPI_pb2 # the _pb2 suffix here has nothing to do with proto version, god knows why google named it this way lol
import socket

TritonBot_IP = "127.0.0.1"
RemoteCONN_Port = 6000
RemoteCMD_Port = 6001
# ...

cmd = RemoteAPI_pb2.Commands()
cmd.enable_ball_auto_capture = True
cmd.mode = 3
cmd.is_world_frame = True
cmd.motion_set_point.x, cmd.motion_set_point.y, cmd.motion_set_point.z = 0, 0, 0
cmd.kicker_set_point.x, cmd.kicker_set_point.y = 0, 0


cmd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd_socket.sendto(cmd.SerializeToString(), (TritonBot_IP, RemoteCMD_Port))
    # ....
    
