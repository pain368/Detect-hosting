import sys
import socket
import subprocess
from urllib.parse import urlparse
from function import *


# TODO: Sprawdzic kod storny


# ------ HELP VARIABLE ------
data_filtr: list = ["inetnum", "netname", "country", "route", "descr"]
# ------ HELP VARIABLE ------

# -------- OPEN FILE --------

print(type(sys.argv[1]))

with open(sys.argv[1], 'r') as file_read_mode:
    data_from_file: list = file_read_mode.readlines()
file_read_mode.close()

# ----- END OPEN FILE -------

# ip = get_address_bulk(data_from_file) <-- dziala


for i in data_from_file:
    res = get_single_address(i.strip("\n"))

    print(res)


# for i in range(0, len(datas )):
#     test: list = datas[i].strip("\n")
#     xx = urlparse(test)
#
#     print(socket.gethostbyname(xx.netloc))
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
