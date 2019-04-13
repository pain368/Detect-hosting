from urllib.parse import urlparse
import socket
from requests import get, post, Request, request


def display_array(array: list):
    """ Display list """
    arr = []
    for i in array:
        arr.append(i)
        print(i)


def clear_list(array):
    """ data modeling """

    zero_array: list = array.split("\n")
    first_array: list = []
    second_array: list = []
    general_array: list = []

    for i in range(0, len(zero_array)):
        first_array.append(zero_array[i].replace(" ", ""))
    for i in range(0, len(first_array)):
        second_array.append(first_array[i].split(":"))
    for i in range(0, len(second_array)):
        if len(second_array[i]) > 1:
            general_array.append(second_array[i])

    return general_array


def get_multiple_address(url_from_file: list):
    """ """

    host_address: list = []
    for i in range(0, len(url_from_file)):
        try:
            url_parse = urlparse(url_from_file[i].strip("\n"))
            hosting_ip: str = socket.gethostbyname(url_parse.netloc)
            host_address.append(hosting_ip)
            return host_address

        except socket.error as err:
            print(err)



def get_single_address(url: str):
    """ """
    try:
        url_parse = urlparse(url.strip("\n"))
        hosting_ip: str = socket.gethostbyname(url_parse.netloc)
        return hosting_ip

    except socket.error as err:
        print(err)


def get_single_response_code(url: str):
    """ Checks whether the web address is working and return the response code"""

    data_response_info: dict = {}
    request_result: str = request("GET", url.strip("\n"))
    data_response_info[url] = request_result

    return data_response_info


def get_multiple_request(url_list: list):
    """ Checks whether www addresses work and return the response code """

    data_response_info: dict = {}

    for i in range(0, len(url_list)):
        request_result: str = request("GET", url_list[i].strip("\n"))
        data_response_info[url_list[i]] = request_result

    return data_response_info
