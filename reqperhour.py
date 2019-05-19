import math
from datetime import *
import matplotlib as md
import matplotlib.pyplot as plt


def reqPerHour(requests):
    plt.title('Request/Hours')

    plt.gcf().autofmt_xdate()
    plt.xlabel('Time (hrs)')

    plt.plot(requests)
    plt.ylabel('Requests')


    plt.savefig("reqPerHours.png")
    plt.show()


    return