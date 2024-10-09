file = open("text.txt", mode = "r")
data = file.readline()

print(data)

file.close()

with open( 'newfile.txt', 'w') as file:
    file.write("This is a new file created!")

# with open function is better at exception handling

try:
    with open("newfile2.txt", mode="r") as file:
        data = file.readline()
        print(data)
except Exception as e:
    print("ERROR:", e)