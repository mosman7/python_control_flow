#
# weather = "raining"
#
# if weather == "cold":       #condition - depending on whether true or false, prints value
#     print("wear a jacket")
# elif weather == "raining":    # if if is not met, 2 if statements will print both
#     print("take an umbrella")
# else:                       # if none of the conditions are met, this will be executed
#     print("dont")

print("Hello, how old are you?")
age = int(input())
if age >= 117:
    print("please input an age below 117")
elif 18 <= age:
    print("You can watch all movies")
elif 16<= age <18:
    print("you cannot watch 18 rated movies")
elif 12<= age < 15:
    print("you cannot watch 16+ movies")
elif age < 12:
    print("parental guidance required")
else:
    print("try again")

