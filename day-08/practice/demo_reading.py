from utilities import read_file,write_json

content=read_file("app.log")
print(content)
write_json("masti_output.json",content)