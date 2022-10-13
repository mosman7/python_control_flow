#data = 0

# while data < 10:
#     print(f"it is working - > {data}")      #f string to combine str and int
#     if data == 5:
#         break           # stops the loop
#     data +=1

# user_prompt = True
#
# while user_prompt:
#     age = input("please enter your age")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print("please use numbers only")
# print(f"your age is {age}")

this_year = 2022
print("how old are you")
age = int(input())

year_born = this_year - age

print(f"You were born in {year_born}")