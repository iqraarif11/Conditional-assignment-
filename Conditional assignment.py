# Task 1: Check age
age = 21
if age >= 18 :
    print("you are an adult.")

# Task 2: Check age with Else
age = 21
if age >= 18 :
     print("you are an adult.")
else:
     print("you are not an adult.")  
 
# Task3: Grading System
marks = 69
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")        

# Task4: Weather Advice
weather = "rainy"
if weather == "rainy":
    print("Take a umbrella")
elif weather == "sunny":
    print("Wear sunglasses")
elif weather == "cloudy": #here we can use only else
    print("It might rain later.")    

# Task 5: Quiz (Feeling Hungry?)
hungry = "Ture"
if hungry :
    print("Go to eat something!")
else:
    print("Maybe have a snake later.")    

# Bonus Fun Task: Mini Chatbot
mood = input("How are you feeling today?")
if mood == "happy":
    print("That a great to hear!") 
elif mood == "sad":
    print("I hope your day gets better.")
elif mood == "bored":
    print("Try reading a book or going for a walk.")
else:
    print("Thanks for sharing your mood!")                 