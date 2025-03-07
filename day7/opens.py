file=open("sample.txt","w")
file.write("hello, this is a sample text!")
file.close()

with open ("sample.txt","w") as file:
    file.write("hello,world!")

#read entire line
with open("sample.txt","r") as file:
    content=file.read
    print(content)

#reding line by line
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())