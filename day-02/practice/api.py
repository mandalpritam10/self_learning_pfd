import requests

api_url= "https://jsonplaceholder.typicode.com/todos/1" 

response = requests.get(url=api_url)

for key,value in response.json().items():
    print(f"{key} : {value}")

for key,value in response.json().items():
    if key== "userId":
        if value in [1,4,5]:
            print("User found")