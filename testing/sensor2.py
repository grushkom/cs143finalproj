import socket
from struct import *

#UDP_IP = "96.49.100.238"
#UDP_IP = "127.0.0.1"
# UDP_IP = socket.gethostbyname(socket.gethostname())
UDP_IP = "172.20.10.11"
print ("Receiver IP: ", UDP_IP)
#UDP_PORT = 6000
# UDP_PORT = int(raw_input ("Enter Port "))
UDP_PORT = 5555
print ("Port: ", UDP_PORT)   
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", data
    # print ("received message: %1.3f %1.3f %1.3f %1.3f", unpack_from ('!f', data, 0), unpack_from ('!f', data, 4), unpack_from ('!f', data, 8), unpack_from ('!f', data, 12))
    # print ("received message: ", "%1.4f" %unpack_from ('!f', data, 0), "%1.4f" %unpack_from ('!f', data, 4), "%1.4f" %unpack_from ('!f', data, 8), "%1.4f" %unpack_from ('!f', data, 12),"%1.4f" %unpack_from ('!f', data, 16), "%1.4f" %unpack_from ('!f', data, 20), "%1.4f" %unpack_from ('!f', data, 24), "%1.4f" %unpack_from ('!f', data, 28),"%1.4f" %unpack_from ('!f', data, 32), "%1.4f" %unpack_from ('!f', data, 36), "%1.4f" %unpack_from ('!f', data, 40), "%1.4f" %unpack_from ('!f', data, 44), "%1.4f" %unpack_from ('!f', data, 48), "%1.4f" %unpack_from ('!f', data, 52), "%1.4f" %unpack_from ('!f', data, 56), "%1.4f" %unpack_from ('!f', data, 60), "%1.4f" %unpack_from ('!f', data, 64), "%1.4f" %unpack_from ('!f', data, 68), "%1.4f" %unpack_from ('!f', data, 72), "%1.4f" %unpack_from ('!f', data, 76), "%1.4f" %unpack_from ('!f', data, 80), "%1.4f" %unpack_from ('!f', data, 84), "%1.4f" %unpack_from ('!f', data, 88), "%1.4f" %unpack_from ('!f', data, 92))

    # print ("received message: ", 
    # 	"%1.4f" %unpack_from ('!f', data, 36), 	# orientation
    # 	"%1.4f" %unpack_from ('!f', data, 40), 
    # 	"%1.4f" %unpack_from ('!f', data, 44)) 
    x = "%1.f" %unpack_from ('!f', data, 36)

    print (x)

    

    # print ("received message: ", 
    # 	"%1.4f" %unpack_from ('!f', data, 36), 	# orientation
    # 	"%1.4f" %unpack_from ('!f', data, 40), 
    # 	"%1.4f" %unpack_from ('!f', data, 44)) 

    # print ("received message: ", 
    # 	"%1.4f" %unpack_from ('!f', data, 0), 	# acceleration
    # 	"%1.4f" %unpack_from ('!f', data, 4), 
    # 	"%1.4f" %unpack_from ('!f', data, 8), 
    # 	"%1.4f" %unpack_from ('!f', data, 12),	# gravity
    # 	"%1.4f" %unpack_from ('!f', data, 16), 
    # 	"%1.4f" %unpack_from ('!f', data, 20), 
    # 	"%1.4f" %unpack_from ('!f', data, 24), 	# rotation
    # 	"%1.4f" %unpack_from ('!f', data, 28),
    # 	"%1.4f" %unpack_from ('!f', data, 32), 
    # 	"%1.4f" %unpack_from ('!f', data, 36), 	# orientation
    # 	"%1.4f" %unpack_from ('!f', data, 40), 
    # 	"%1.4f" %unpack_from ('!f', data, 44), 
    # 	"%1.4f" %unpack_from ('!f', data, 48), 
    # 	"%1.4f" %unpack_from ('!f', data, 52), 
    # 	"%1.4f" %unpack_from ('!f', data, 56), 
    # 	"%1.4f" %unpack_from ('!f', data, 60), 
    # 	"%1.4f" %unpack_from ('!f', data, 64), 
    # 	"%1.4f" %unpack_from ('!f', data, 68), 
    # 	"%1.4f" %unpack_from ('!f', data, 72), 
    # 	"%1.4f" %unpack_from ('!f', data, 76), 
    # 	"%1.4f" %unpack_from ('!f', data, 80), 
    # 	"%1.4f" %unpack_from ('!f', data, 84), 
    # 	"%1.4f" %unpack_from ('!f', data, 88), 
    # 	"%1.4f" %unpack_from ('!f', data, 92))