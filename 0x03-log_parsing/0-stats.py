#!/usr/bin/python3
""" Log parsing. """
import re
import sys


def printStat(info):
    """ Print info. """
    print("File size: {}".format(info["file_size"]))
    for key, value in info["status_code"].items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    count = 0
    info = {
        "file_size": 0,
        "status_code": {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
    }
    rgx = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)'
                     r'{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\s'
                     r'-'
                     r'\s\[\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])'
                     r'\s\d{2}:\d{2}:\d{2}\.\d+\]'
                     r'\s\"GET\s\/projects\/260\sHTTP\/1.1\"\s\d+\s\d+$')
    try:
        for line in sys.stdin:
            count += 1
            if re.match(rgx, line):
                status_code = line.split('"')[2].split(" ")[1]
                file_size = line.split('"')[2].split(" ")[2]
                count %= 10
                if status_code in info["status_code"].keys():
                    info["status_code"][status_code] += 1
                    info["file_size"] += int(file_size)
                    if count == 0:
                        printStat(info)
    except KeyboardInterrupt:
        printStat(info)
        raise
