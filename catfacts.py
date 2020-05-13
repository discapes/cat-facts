import requests

url = "https://cat-fact.herokuapp.com/facts/random"
params = {'animal_type': 'horse', 'amount': '1'}
response = requests.get(url = url, params = params)
x = response.json()

print(x['text'])
