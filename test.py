Name = input("Enter your name: ") 

Age = input("Enter your age: ") 

 

print("Choose an activity:") 

print("1. Music Jam Session (2 hours, easy, $5 fee)") 

print("2. Sports Leadership Training (4 hours, moderate $10 fee)") 

print("3. Sports Leadership Training (4 hours, Challenging, $12 fee)") 

Activity = input("Enter the number of your chosen activity: ") 
Activity =["1. Music Jam Session", "2. Sports Leadership Training", "3. Sports Leadership Training" ]

print("Meal options:") 

print("1. Standard") 

print("2. Vegetarian") 

print("3. Dairy-free") 

print("4. No meal") 

Meal = input("Enter the number of your meal choice: ") 

 

yn = input(f"{Name}, age {Age}, has chosen {Activity}, Meal option: {Meal}. The total cost is . Are you attending (yes/no): ") 

if "yes":
    print(f"{Name} is confirmed for {Activity}, see you there!")

if "no":
    print(f"{Name} has chosen to cancel.")