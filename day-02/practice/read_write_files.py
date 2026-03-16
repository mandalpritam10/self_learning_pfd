"""
manual way to handle a file
"""

# file = open("demo.txt") #OPEN
# content=file.read()
# print(content) # OPERATION
# file.close() # CLOSE

"""
only read the file
"""
# with open("demo.txt","r") as file:
#     content=file.read()
#     print(content)

"""
adding some new content
"""
# with open("demo.txt","a") as file:
#     file.write("\naapka kya haal hai bro")


with open("demo.txt","r") as file:
    content=file.read()
    print(content)


"""
Look below, This is how we can actually access and do our operations on a file that is not inside the same folder, which is in a different location.
here the example is for practice.py which is inside python_for_devops and in same hierarchy level of self_learning_pfd. we want to run python practice.py,
so this is the code:
"""

# import os

# base_dir=os.path.dirname(__file__)

# file_path=os.path.join(
#     base_dir,
#     "self_learning_pfd",
#     "day-02",
#     "practice",
#     "demo.txt"
# )

# with open(file_path,"r") as file:
#     print(file.read())