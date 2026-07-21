with open("file.txt","w") as file:
    file.write("hello world")
with open("file.txt","r") as file:
    print(file.read())
with open("file1.txt","a") as file:
    file.write("python programming")
with open("file1.txt","r") as file:
    print(file.read())