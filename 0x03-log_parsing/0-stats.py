#!/usr/bin/python3
""" Log parsing. """
import sys


def printStat(info):
    """ Print info. """
    print("File size: {}".format(info["file_size"]))
    for key, value in info["status_code"].items():
        if value != 0:
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
    try:
        for line in sys.stdin:
            count += 1
            try:
                status_code = line.split('"')[2].split(" ")[1]
                file_size = line.split('"')[2].split(" ")[2]
                if status_code in info["status_code"].keys():
                    info["status_code"][status_code] += 1
                    info["file_size"] += int(file_size)
            except Exception:
                pass
            count %= 10
            if count == 0:
                printStat(info)
    except KeyboardInterrupt:
        printStat(info)
        raise
    printStat(info)
