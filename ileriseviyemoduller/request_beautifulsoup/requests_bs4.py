import requests

url = "https://yellowpages.com.tr/ara?q=Ankara"

response = requests.get(url)

print(response)