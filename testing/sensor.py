import socket, traceback
import time

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

# data:
# 111853.68583, 3,   0.280,  3.041,  9.180, 4,  -0.009, -0.023, -0.026, 5, -12.900,-38.700,-25.900
# 3: accelerometer: 		X (2), Y (3), Z(4)
# 4: gyroscope: 			X (6), Y (7), Z (8)
# 5: magnetic field: 		X (10),Y(11), Z (12)

print("Success binding")
while 1:
        try:
                message, address = s.recvfrom(8192)
                messageString = message.decode("utf-8")
                # 111853.68583, 3,   0.280,  3.041,  9.180, 4,  -0.009, -0.023, -0.026, 5, -12.900,-38.700,-25.900
                # print(messageString)
                data = messageString.split(',')
                # print(data)
                print(data[7])
                time.sleep(0.1)

        except (KeyboardInterrupt, SystemExit):
                raise
        except:
                traceback.print_exc()
