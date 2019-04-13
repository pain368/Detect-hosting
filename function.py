from urllib.parse import urlparse
import socket


def displeyArray(array: list):

    arr = []
    for i in array:
        arr.append(i)
        print(i)


def cleare_array(array):

    zero_array: list = array.split("\n")
    first_array: list = []
    second_array: list = []
    general_array: list = []

    for i in range(0, len(zero_array)):
        first_array.append(zero_array[i].replace(" ", ""))
    for i in range(0, len(first_array)):
        second_array.append(first_array[i].split(":"))
    for i in range(0, len(second_array)):
        if len(second_array[i])>1:
            general_array.append(second_array[i])
    return general_array



def get_address(urlFromfile: list):

    aa = urlparse("https://www.kross.pl")
    get_host_name: str = socket.gethostbyname(aa.netloc)

    return get_host_name
