myList=[1,4.0,True,"Pritam"]
print(type(myList))
print(myList)

clouds=list()
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("alibaba")
clouds.append("ibm")
clouds.append("utho")

print(clouds)
print(f"Length of the list is: {len(clouds)}")
print(f"{clouds[-1]} is Indian cloud service")
print(f"{clouds[0]} is the market leader")

print("we can do such operations in this list: ", dir(clouds))

print(clouds.append.__doc__)


for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} is market leader of cloud services")
    elif cloud == "utho":
        print(f"{cloud} is indian cloud service")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} will be covered in this course")
    else:
        print(f"{cloud} is one of the other cloud services")