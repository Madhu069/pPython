# Pet food selector


pet = "Dog"

age = 2

if pet == "Dog" and age <= 2:
    food = "Puppy food"
elif pet == "Dog" and age > 2:
    food = "Adult dog food"
elif pet == "Cat" and age > 5:
    food = "Senior cat food"
elif pet == "Cat" and age < 5:
    food = "Adult cat food"
else:
    food = "Regular pet food"



print(food, "is for him")

