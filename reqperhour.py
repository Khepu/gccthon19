import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

def reqperhour(req):

    plt.plot(req)
    plt.gcf().autofmt_xdate()
    plt.show()