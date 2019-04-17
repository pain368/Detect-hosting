from urllib.parse import urlparse
import socket
from requests import request
import subprocess
import concurrent.futures


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


def get_multiple_address_ip(url_from_file: list):
    """ """

    host_address: list = []
    for i in range(0, len(url_from_file)):
        url_parse = urlparse(url_from_file[i].strip("\n"))
        hosting_ip: str = socket.gethostbyname(url_parse.netloc)
        host_address.append(hosting_ip)

    return host_address


def get_single_address_ip(url: str):
    """ """
    try:
        url_parse = urlparse(url.strip("\n"))
        hosting_ip: str = socket.gethostbyname(url_parse.netloc)
        return hosting_ip

    except socket.error as err:
        print(err)


def get_single_response_code(url: str):
    """ Checks whether the web address is working and return the response code"""
    try:
        request_result = request("GET", url.strip("\n"))
        return request_result.status_code

    except Exception as err:
        return err


def get_multiple_response_code(url: list, timeout: int = 0):
    """ Checks whether www addresses work and return the response code """

    print(timeout)
    data_response_info: dict = {}
    for i in range(0, len(url)):
        request_result = request("GET", url[i].strip("\n"))
        data_response_info[url[i]] = request_result.status_code

    return data_response_info


def get_response_code_threading(function, url_list: list):
    """
    :param url_list: pass address URL as a list
    :type function: just a function
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        # result {url:resp_code}
        result: dict = {}

        future_to_url: dict = {executor.submit(function, link): link for link in url_list}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:

                result[url.strip("\n")] = future.result()
            except Exception as err:
                print('%r generated an exception: %s' % (url, err))

    return result

