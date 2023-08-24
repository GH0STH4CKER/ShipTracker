from requests import Session
import json,webbrowser

session = Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'

ship = input("Ship Name/IMO : ")

url = "https://services-etac.sinay.ai/api/vessels?search="+ship

resp = session.get(url)

if resp.ok :

    data = json.loads(resp.text)

    for key, value in data.items():
        if isinstance(value, list):
            for item in value:
                print('\n')
                for inner_key, inner_value in item.items():
                    print(f"{inner_key}: {inner_value}")
        else:
            print(f"{key}: {value}")

    lat = data['data'][0]['latitude']
    lon = data['data'][0]['longitude']

    webbrowser.open(f'http://www.google.com/maps/place/{lat},{lon}') 
else:
    print(resp.reason)
