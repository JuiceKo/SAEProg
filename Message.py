import platform
import os
import psutil
import socket

while True:
    msg = input()
    if msg == "OS":
        print(platform.system(),platform.release()," Version :",platform.version())

    #"""elif msg == "RAM":
    #        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
    #       mem_gib = mem_bytes / (1024. ** 3)  # e.g. 3.74
    #      print('Nous avons en total',psutil.virtual_memory().total, "Bytes de RAM")"""

    elif msg == "NOM":
        print(socket.gethostname())

    elif msg == "IP":
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        print("Host Name is:" + h_name)
        print("Computer IP Address is:" + IP_addres)

    elif msg == "CPU":
        # Getting % usage of virtual_memory ( 3rd field)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        # Getting usage of virtual_memory in GB ( 4th field)
        print('RAM Used (GB):', psutil.virtual_memory()[3] / 1000000000)



