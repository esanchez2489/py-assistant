import urllib.request, urllib.parse, urllib.error
import json 

def weather(location):
    token = 'a5e4fd96244d0b1183b3fb7753da5850'

    url = 'http://api.openweathermap.org/data/2.5/weather?'
    address = location
    parms = dict()
    parms ['q'] = address
    parms ['appid'] = token
    parms ['units'] = 'imperial'

    url = url + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url)
    #print (url)
    data = uh.read().decode()
    js = json.loads(data)
    #print (json.dumps(js, indent=4))
    temperature = ''
    try:
        temperature = js['main']['temp']
        wind_speed = js['wind']['speed']
    except:
        print ('could not get address. Please try again')

    if temperature != '':
        return (round(temperature),round(wind_speed))

