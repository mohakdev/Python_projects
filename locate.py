import pygeoip
gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('25.129.235.47')
for key , val in res.items():
    print('%S : %S' % (key,val))