import requestByCountry
import Ip2location

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

x=[1029, 2223, 6549, 6727, 4234, 2048, 3148, 6544, 4404, 1795, 3179, 1104, 2084, 2164, 8622, 1078, 420,1163,8843,1042]
for i in range(len(x)):
    x[i] = x[i]/68400

print(x)






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




