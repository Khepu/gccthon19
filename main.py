from pandas import read_csv
import re


def main():
    data = read_csv("./datasets/website-access.data", sep=" ", header=None)

    codes = data[4].values
    fivexx = tuple(filter(lambda c: c >= 500 and c < 600, codes))

    print(len(fivexx))

    ips = data[0]
    unique_ips = len(set(ips))

    print(len(ips))
    print(unique_ips)

    dates = data[1]


def getHour(date, hour):
    return re.search("^$", date)


data = read_csv("./datasets/website-access.data", sep=" ", header=None)



if __name__ == "__main__":
    main()
