print("Today's date?");
date = input()
print("Breakfast calories?")
breakfast = input()
print("Lunch calories?")
lunch = input()
print("Dinner calories?")
dinner = input()
print("Snack calories?")
snach = input()
result = int(breakfast) + int(lunch) + int(dinner) + int(snach)
print("\r\n")
print("Calorie content for " + str(date) + ": " + str(result))
