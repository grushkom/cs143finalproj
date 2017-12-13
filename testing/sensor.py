import socket, traceback

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

print("Success binding")
while 1:
        try:
                message, address = s.recvfrom(8192)
                messageString = message.decode("utf-8")
                print(messageString)
        except (KeyboardInterrupt, SystemExit):
                raise
        except:
                traceback.print_exc()

# import socket, traceback

# host = ''
# port = 5555

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# s.bind((host, port))

# #used for debugging

# print("Success binding")
# while 1:
#     message, address = s.recvfrom(8192)
#     messageString = message.decode("utf-8")
#     print(messageString)
