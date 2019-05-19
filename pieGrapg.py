import requestByCountry
import Ip2location
import matplotlib.pyplot as plt

ip = requestByCountry.reqByCou()
print(ip)
c1 = Ip2location.ip2loc("1.2.169.95")
c2 = Ip2location.ip2loc("103.36.79.144")
c3 = Ip2location.ip2loc("115.221.121.44")
c4 = Ip2location.ip2loc("121.225.26.201")
c5 = Ip2location.ip2loc("182.34.27.162")
c6 = Ip2location.ip2loc("183.87.255.54")
c7 = Ip2location.ip2loc("209.133.212.79")
c8 = Ip2location.ip2loc("220.243.135.5")
c9 = Ip2location.ip2loc("31.184.238.22")
c10 = Ip2location.ip2loc("39.36.99.88")
c11= Ip2location.ip2loc("45.61.164.120")
c12 = Ip2location.ip2loc("5.13.35.65")
c13= Ip2location.ip2loc("54.36.149.52")
c14= Ip2location.ip2loc("54.36.149.94")
c15 = Ip2location.ip2loc("62.109.16.162")
c16 = Ip2location.ip2loc("69.46.0.142")
c17 = Ip2location.ip2loc("75.140.82.208")
c18= Ip2location.ip2loc("86.125.112.230")
c19 = Ip2location.ip2loc("87.251.81.179")
c20= Ip2location.ip2loc("91.138.198.224")

sumChina = ip[2]+ip[3]+ip[4]+ip[7]
sumIndia = ip[1]+ip[5]
sumUn = ip[6]+ip[10]+ip[15]+ip[16]
sumRus = ip[8]+ip[14]+ip[18]
sumRo = ip[11]+ip[17]
sumFr = ip[12]+ip[13]


x=[1029, sumIndia, sumChina, sumUn, sumRus, 1795, sumRo, sumFr, 1042]
for i in range(len(x)):
     x[i] = x[i]/68400

countries = [c1,c2,c3,c7,c9,c10,c12,c14,c20]

for i in countries:
    labels = countries

for i in x:
    sizes=x

#tailand pakistan
explode = (0,0,0.1,0.1,0.1,0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("Pie.png")






# Thailand              1.2.169.95        1029
# India                 103.36.79.144     2223
# China                 115.221.121.44    6549
# China                 121.225.26.201    6727
# China                 182.34.27.162     4234
# India                 183.87.255.54     2048
# United States         209.133.212.79    3148
# China                 220.243.135.5     6544
# Russian Federation    31.184.238.22     4404
# Pakistan              39.36.99.88       1795
# United States         45.61.164.120     3179
# Romania               5.13.35.65        1104
# France                54.36.149.52      2084
# France                54.36.149.94      2164
# Russian Federation    62.109.16.162     8622
# United States         69.46.0.142       1078
# United States         75.140.82.208      420
# Romania               86.125.112.230    1163
# Russian Federation    87.251.81.179     8843
# Greece                91.138.198.224    1042




