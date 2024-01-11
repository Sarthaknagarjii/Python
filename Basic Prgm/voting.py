age = int(input("Enter your age : "))
if age < 18:
    print("You are not eligible for voting")
elif age == 18:
    print("Now you can give your vote in upcoming election")
else:
    print("You are already eligible")
