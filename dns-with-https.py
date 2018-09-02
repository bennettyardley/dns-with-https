import requests
import uuid

url = raw_input("Enter URL (ex. google.com): ")
rand = str(uuid.uuid4())
response = requests.get('https://dns.google.com/resolve?name=' + url + '&random_padding=' + rand)
data = response.json()
ip = data['Answer'][0]['data']
cd = data['CD']

if not cd:
    print(url + " -> " + str(ip))
else:
    "HTTPS was not used"
