from pandas import read_csv
from helpers import mapt

def main():
    data = read_csv("./datasets/website-access.data", sep=" ", header=None)

    codes = mapt(lambda d: d[4], data.values)
    fivexx = tuple(filter(lambda c: c >= 500 and c < 600, codes))

    print(len(fivexx))

    ips = data[0]
    unique_ips = len(set(ips))

    print(len(ips))
    print(unique_ips)

if __name__ == "__main__":
    main()
