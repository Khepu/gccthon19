from pandas import read_csv

def main():
    data = read_csv("./datasets/website-access.data", sep=" ", header=None)

    codes = data[4].values
    fivexx = tuple(filter(lambda c: c >= 500 and c < 600, codes))

    print("Number of Request: "+str(len(fivexx)))

    ips = data[0]
    unique_ips = len(set(ips))

    print("Total traffic: "+str(len(ips)))
    print("unique IPs: "+str(unique_ips))


if __name__ == "__main__":
    main()

