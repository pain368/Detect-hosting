import sys
import subprocess
from function import *

# ------ HELP VARIABLE ------

data_filter: list = ["inetnum", "netname", "country", "route", "descr"]

# ---------------------------


# -------- OPEN FILE --------

with open(sys.argv[1], 'r') as file_read_mode:
    data_from_file: list = file_read_mode.readlines()
file_read_mode.close()

# ----- END OPEN FILE -------


data_to_display = get_multiple_address(data_from_file)

for ip in data_to_display:

    data_hosting: bytes = subprocess.check_output(["whois", '{}'.format(ip)])
    data_decode: str = data_hosting.decode("utf-8")
    data: list = clear_list(data_decode)

    for i in range(0, len(data)):
        for j in range(0, len(data_filter)):
            if data_filter[j] in data[i]:
                print(" : ".join(data[i]))
    print("------------------------")
