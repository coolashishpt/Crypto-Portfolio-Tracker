
import threading
import requests

def reloadapi():
    threading.Timer(1.0, reloadapi).start()
    response = requests.get('https://api.wazirx.com/api/v2/tickers')
    data = response.json()["btcinr"]["last"]
    print(data)

reloadapi()



 
