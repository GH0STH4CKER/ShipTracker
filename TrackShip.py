from requests import Session
import json,webbrowser
# create session object
####
import logging
import http.client
http.client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
####

session = Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'

ship = input("Ship Name/IMO : ")

url = r"https://services-etac.sinay.ai/api/vessels?search={ship}"

resp = session.get(url)
#res = get(url,headers={'user-agent':ua,
#"cookie": "_gcl_au=1.1.588940811.1684131703; intercom-id-u8yz6vse=fac67945-63d4-4c88-8871-aef2ca0f6b1d; intercom-session-u8yz6vse=; intercom-device-id-u8yz6vse=cfdb1168-a23f-4de5-82e0-8738b7f4f0a9; __hstc=234908254.b680a84520a16c145cb7503404276044.1684131706061.1684131706061.1684131706061.1; hubspotutk=b680a84520a16c145cb7503404276044; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19IRq1bOCTTafKqqGR7N6p90R%2Fj%2B4vqFDqd7rZAKrfomgKBddQIGQ5Y; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2B6Aw9slA5xxbkKIKvi6zmYWkf3F5uItjQ%3D; _hjSessionUser_2581584=eyJpZCI6ImQ2NWRkYzExLTY5ZGEtNTFkZS05OWVlLTFjNzFhNDEwMGEwZiIsImNyZWF0ZWQiOjE2ODQxMzE3MzQyODIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2147704=eyJpZCI6IjRmYmZkNmM2LWRiYmItNTU2NS1hMDNhLTA1MzgxOWE1YzY1YiIsImNyZWF0ZWQiOjE2ODQxMzE3MDQ1MjQsImV4aXN0aW5nIjp0cnVlfQ==; rl_user_id=RudderEncrypt%3AU2FsdGVkX19PzRtEUN6J52V4OPiEDvE%2FklZO6J45Ojc%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BWggapN3ALgNLtKTHHEHLPJG90XHoaGiucKkfB8feft663F1E9pYyG; rl_group_id=RudderEncrypt%3AU2FsdGVkX19B%2BK0oWzkOATb6s7RUPLOQ77szirAdwnQ%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18tYrbrWB7xEVzaNL70iEhu4Lnl4%2FJ1jvk%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19viR8iuI1EIDPUlQuo4O1r%2FWMiNrGT1ElDQ07NPfJGRZ808PfyT0SnZ2XeQRqcXkVPfeNMhUO4XA%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX19cN%2BortZOCVN8at6FVu5EUBU0wTBePJrlNH9pw6rZmpfJ%2BsSHqCvXe%2BjA3o79yaPpc7SoaX61ioG2HcNNAhJKoxf2PBTqQpxScLBiQ9TK6NgGFkVGgFbnfA74GH9rGav6XJ5JsNvlvxg%3D%3D; _uetvid=d32af210f2e811eda63239d7ce7ae00e; _gac_UA-36380687-3=1.1684132149.CjwKCAjwjYKjBhB5EiwAiFdSfqUp_qu5hPeNPvWzErrGzDuCBYJG2Unhur7fWlxA-3UXyXMGJDZ1LxoC5dEQAvD_BwE; _gcl_aw=GCL.1684132149.CjwKCAjwjYKjBhB5EiwAiFdSfqUp_qu5hPeNPvWzErrGzDuCBYJG2Unhur7fWlxA-3UXyXMGJDZ1LxoC5dEQAvD_BwE; _ga=GA1.2.1042897012.1684131703; _ga_NWCS8SL817=GS1.1.1684131703.1.1.1684132207.0.0.0; _ga_XWX1P1LSSG=GS1.1.1684131730.1.1.1684134037.0.0.0"})

if resp.ok :

    data = json.loads(resp.text)
    #for i in data:
        #print(i,data[i])

    lat = data['data'][0]['latitude']
    lon = data['data'][0]['longitude']

    webbrowser.open(f'http://www.google.com/maps/place/{lat},{lon}') 
else:
    print(resp.reason)
