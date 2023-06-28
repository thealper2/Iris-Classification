import requests

test = {
   "sepal_length": 1.2,
   "sepal_width": 2.3,
   "petal_length": 1.4,
   "petal_width": 2.8
 }

url = "http://127.0.0.1:8000/predict"
response = requests.post(url, json=test)
print(response.content.decode("utf-8"))
