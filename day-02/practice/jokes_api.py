import requests

"""
As a devops engineer, you will have to navigate through multiple
external endpoints, and you should know how to switch them with Python
"""

pj_url = "https://official-joke-api.appspot.com/random_joke"

dadjoke_url = "https://icanhazdadjoke.com/"

def get_jokes(url_type):

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url=url_type, headers=headers)
    data = response.json()

    if url_type == pj_url:
        return data["setup"] + " " + data["punchline"]

    if url_type == dadjoke_url:
        return data["joke"]


mood = input("Enter which one you wanna listen? (type dad or pj): ")

if mood == "pj":
    url_type = pj_url
elif mood == "dad":
    url_type = dadjoke_url
else:
    print("type exact dad or pj specifically")
    exit()

final_joke = get_jokes(url_type)

print(final_joke)