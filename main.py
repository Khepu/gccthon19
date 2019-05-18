from helpers import append
from pandas import read_csv
from functools import reduce

def isHour(date, h):
    return True if date.split(":")[1] == h else False

def padToTwo(h):
    return str(h) if h >= 10 else "0" + str(h)

def main():
    data = read_csv("./datasets/website-access.data", sep=" ", header=None)

    codes = data[4].values
    fivexx = tuple(filter(lambda c: c >= 500 and c < 600, codes))

    print(len(fivexx))

    ips = data[0]
    unique_ips = len(set(ips))

    print(len(ips))
    print(unique_ips)
    sum = 0
    requestsPerHour = list(range(24))
    for i in range(24):
        requestsPerHour[i] = len(tuple(filter(lambda date: isHour(date, padToTwo(i)), data[1])))
    print(requestsPerHour)

if __name__ == "__main__":
    main()
