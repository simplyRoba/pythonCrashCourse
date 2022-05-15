# 7-1
car = input("What kind of car do you want? ")
print(f"Let me see if i can find you a {car.title()}.")

# 7-2
people_count = int(input("How many people want to eat? "))
if people_count > 8:
    print("You have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3
number = int(input("Tell me a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10.")
