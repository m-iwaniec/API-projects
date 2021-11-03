import requests


request = requests.get("http://api.open-notify.org")
print(request.text)

print(request.status_code)
# code 200 is ok

request2 = requests.get("http://api.open-notify.org/fake-endpoint")
print(request2.status_code)
