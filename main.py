import pygeoip
import gmplot
import webbrowser

gip = pygeoip.GeoIP("GeoLiteCity.dat")
ip = input("Hey User! Enter IP Address to locate : ")
res = gip.record_by_addr(ip)
if res:
    for key, val in res.items():
        print('%s : %s' % (key, val))        
        lat = [res.get('latitude')]
        lon = [res.get('longitude')]
        gmap = gmplot.GoogleMapPlotter(res.get('latitude'), res.get('longitude'), 15)
        gmap.scatter(lat, lon, 'blue',size = 50, marker=False)
        gmap.draw('map.html')
    url = r'C:\Users\windows\Desktop\PythonProjects\TrackLocationUsingIPAddress\map.html'
    webbrowser.open(url,new=2)
else:
    print(':( Not Found!')
