info={
    "name" : "Pritam",
    "city" : "basirhat",
    "age" : 23,
    "gender" : "male",
    "favourites" : ["rohit","mom","peace"],
    "company" : "siemens"
}

for i in info.keys():
    print(i)

for j in info.values():
    print(j)

for key,value in info.items():
    print(f"{key} : {value}")

print(f"My city is: {info["city"]}")
print(f"I love {info.get("favourite","not found")}")
print("we can do such operations in a dictionary: ",
dir(info))

print(info.update({"origin" : "Indian"}))

print(info)

print(info.pop.__doc__)