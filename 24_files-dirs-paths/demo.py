# import data/graph.dot and data/sheet.csv
# and print the contents of both files

# one way to read a file
with open("data/graph.dot") as file:
    contents = file.read()
    # print(contents)
    
with open("data/sheet.csv") as file:
    contents = file.read()
    # print(contents)
    
# scan through the lines of sheet.csv and search for a specific string

with open("data/sheet.csv") as file:
    contents = file.readlines()
    for row in contents:
        if "511" in row:
            print(row)
            
# modify the contents of a file
with open("data/sheet.csv", mode="a") as file:
    file.write("\nNew row")
    
# create a new file
with open("data/new_file.txt", mode="w") as file:
    file.write("New text.")