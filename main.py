import requestByCountry
from helpers import append
from pandas import read_csv
import pandas as pd
import Ip2location
from functools import reduce
from helpers import mapt, append, compose, flatten
from pandas import read_csv
from functools import reduce, partial
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from re import escape

def classify(xtrain, ttrain, xtest):
    model = SVC(C = 0.1,
                kernel = "rbf",
                gamma = 10)
    fitted_model = model.fit(xtrain, ttrain)
    return fitted_model.predict(xtest)

def kmeans(x):
    model = KMeans(n_clusters = 8,
                   n_init = 10,
                   max_iter = 100000,
                   tol = 1e-2,
                   precompute_distances = True,
                   n_jobs = 20,
                   algorithm = "full")

    model.fit(x)
    return model.cluster_centers_

def vectorize(data):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data)

    features = vectorizer.get_feature_names()
    print(len(features))
    #print(X[1].toarray())
    return X.toarray()

def append3(a, b, c):
    return append(a, append(b, c))

def isHour(date, h):
    return True if date.split(":")[1] == h else False

def padToTwo(h):
    return str(h) if h >= 10 else "0" + str(h)

def preprocess(requests):
    #Splitting the requests into [METHOD, URL, PROTOCOL]
    #also dropping PROTOCOL
    requests = mapt(lambda r: r.split(" ")[0:-1], requests)
    print(requests[0])
    #Splitting URL into path and query string
    requests = mapt(lambda r: append([r[0]], r[1].split("?")), requests)
    print(requests[0])
    #Transform GET into 0 and POST into 1
    requests = mapt(lambda r: append([0] if r[0] == "GET" else [1], r[1:3]), requests)
    print(requests[0])
    return requests



def main():
    data = read_csv("datasets/website-access.data", sep=" ", header=None)
    codes = data[4].values
    fivexx = tuple(filter(lambda c: c >= 500 and c < 600, codes))
    print(len(fivexx))
    ips = data[0]
    unique_ips = set(ips)
    totalTraffic = data[5].sum()
    print(totalTraffic)
    countries = list(zip(list(map(Ip2location.ip2loc, unique_ips)), unique_ips))
    print(countries)
    print(len(ips))
    print(len(unique_ips))
    sum = 0
    requestsPerHour = list(range(24))
    for i in range(24):
        requestsPerHour[i] = len(tuple(filter(lambda date: isHour(date, padToTwo(i)), data[1])))
    #print(requestsPerHour)



    vectorized_urls = vectorize(data[3])
    #    vectorize_preproc = partial(vectorize, preprocessed_data)
    #    print(mapt(vectorize_preproc, range(1,3)))
    #    requests = flatten(mapt(vectorize_preproc, range(3)))
    #   print(requests)

    to_cluster = mapt(lambda i: append3(vectorized_urls[i], [data[4][i]], [data[5][i]]), range(len(vectorized_urls)))
    clusters = kmeans(to_cluster)
    print(clusters)
    ttrain = range(len(clusters))
    test_set = read_csv("./datasets/website-access-samples.data", sep=" ", header=None)

    vectorized_test = vectorize(test_set[0])
    #    xtest = list(range(len(test_set)))
    #    for i in range(len(test_set)):
    #        xtest[i] = flatten([vectorized_test[i], [test_set[1][i]], [test_set[2][i]]])
    output = open("out.txt", "w+")
    result = classify(clusters, ttrain, to_cluster)
    for i in result:
        output.write(str(i) + "\n")

if __name__ == "__main__":
    main()
