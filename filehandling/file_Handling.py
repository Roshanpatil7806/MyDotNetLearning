import json

# 1. Create and write to a file
with open("student.txt", "w") as file:
    file.write("Name: Roshan\n")
    file.write("Age: 22\n")
    file.write("Course: Python\n")
    file.write("Topic: File Handling\n")

print("File created and data written successfully!")

 
# 2. Read the file
with open("student.txt", "r") as file:
    data = file.read()

print("\nFile Content:")
print(data)


# 3. Append data to the file
with open("student.txt", "a") as file:
    file.write("Status: Learning Python\n")

print("Data appended successfully!")


# 4. Read file line by line
with open("student.txt", "r") as file:
    print("\nReading file line by line:")

    for line in file:
        print(line.strip())


# 5. Count number of characters
with open("student.txt", "r") as file:
    data = file.read()

print("\nNumber of characters:", len(data))

with open("policies.json", "w") as policy_file:
    policies = {

        
    }
    json.dump(policies, policy_file)

with open("roshan.txt", "w") as s:
    s.write("Name: Roshan\n")
    s.write("Age: 22\n")
    s.write("Course: Python\n")
    s.write("Topic: File Handling\n")

with open("roshan.txt", "a") as s:
    s.write("Status: Learning Python\n")

with open("roshan.txt", "r") as s:
    data = s.read()
    print("File Content:")
    print(data)