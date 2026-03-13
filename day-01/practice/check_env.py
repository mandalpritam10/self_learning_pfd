env=input("Enter the environment: ")

print("The environment is: ",env)

if env== "prd":
    print("don't deploy on friday")
elif env== "stg":
    print("take backup and test well")
else:
    print("safe to deploy on any day")

# a=int(input("enter a: "))
# b=int(input("enter b: "))

# print("add: ",a+b)
# print("division: ",a/b)