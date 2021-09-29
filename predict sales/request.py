import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'int_rate':5, 'installment':200, 'credit score':400})

print(r.json())