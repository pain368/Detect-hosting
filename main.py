import sys
import socket
import subprocess
from urllib.parse import urlparse
from function import displeyArray, cleare_array
from urllib.parse import urlparse


# ------ HELP VARIABLE ------
data_filtr: list = ["inetnum", "netname", "country", "route", "descr"]
# ------ HELP VARIABLE ------

# -------- OPEN FILE --------

print(type(sys.argv[1]))

with open(sys.argv[1], 'r') as file_readMode:
    datas: list = file_readMode.readlines()

# ---------------------------

for i in range(0, len(datas)):
    test: list = datas[i].strip("\n")
    xx = urlparse(test)
    print(type(xx))
    print(socket.gethostbyname(xx.netloc))


object_socket: classmethod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# data_hostin: bytes = subprocess.check_output(["whois", '80.72.35.35'])
# data_decode: str = data_hostin.decode("utf-8")
# data: list = cleare_array(data_decode)


# xx: list = []
#
# for i in range(0, len(data)):
#     for j in range(0, len(data_filtr)):
#         if data_filtr[j] in data[i]:
#             print(" : ".join(data[i]))
# print("------------------------")
