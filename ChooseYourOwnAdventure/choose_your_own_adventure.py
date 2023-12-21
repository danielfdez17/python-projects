name = input("Type you name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left of right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk or swim: ").lower()
    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You loose!")
elif answer == "right":
    print()
else:
    print("Not a valid option. You loose!")


print(f"Thank you for playing {name}")