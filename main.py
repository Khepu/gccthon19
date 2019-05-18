
from helpers import append
from pandas import read_csv
import pandas as pd
import Ip2location
from functools import reduce
def isHour(date, h):
    return True if date.split(":")[1] == h else False

def padToTwo(h):
    return str(h) if h >= 10 else "0" + str(h)

def main():
    data = read_csv("datasets/website-access.data", sep=" ", header=None)

    codes = data[4].values
    fivexx = tuple(filter(lambda c: c >= 500 and c < 600, codes))

    print(len(fivexx))

    ips = data[0]
    unique_ips = set(ips)

    # for i in unique_ips:
    #     listofip=i
    #     ok=Ip2location.ip2loc(i)
    #     print(ok)

    countries = list(zip(list(map(Ip2location.ip2loc, unique_ips)), unique_ips))
    print(countries)
    print(len(ips))
    print(len(unique_ips))

    ok=Ip2location.ip2loc("31.184.238.22")
    print(ok)
    sum = 0
    requestsPerHour = list(range(24))
    for i in range(24):
        requestsPerHour[i] = len(tuple(filter(lambda date: isHour(date, padToTwo(i)), data[1])))
    print(requestsPerHour)

if __name__ == "__main__":
    main()
