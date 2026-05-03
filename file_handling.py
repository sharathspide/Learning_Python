file = open("sample.txt","w")
file.write("Hello, this is my first file!")
file.close()

file = open("sample.txt","r")
content = file.read()
print(content)
file.close()

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

with open("sample.txt", "a") as file:
    file.write("\nThis is a new line added later.")
    
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())