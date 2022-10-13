#create dictionary student_data
#iterate thru the dict
#using control flow - if elif else
#print all values
#print key with matching value name

student_name = {
    "name": "Mohamed",
    "stream": "devops",
    "completed": "eng130"
}

#for i in student_name.values():
   # print(i)

for i in student_name.values():
    if i == "name":
        print(f"your name is {student_name[x]}")
    elif i == "stream":
        print(f"You are studying {student_name[x]}")
    elif i == "completed":
        print(f"you are in the {student_name[x]} course")

