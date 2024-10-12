unit = ""
sex = ""
weight = 0.0
height = 0.0
age = 0
activity = 0
diet = 0

activityLevels = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
    }

# Calculates the user's BMI depending on user's unit of preference
def BMI(imperial, weight, height):
    if (imperial):
        return (weight / (height * height) * 703.0)
    else:
        return weight / ((height / 100)  ** 2)


# Calculates the user's BMR depending on user's unit of preference
# Many of the 'magic numbers' are conversion factors for the BMR from the Mifflen-St Jeor equation
def BMR(imperial, weight, height, sex, age):
    if (imperial):
        if "male" in sex.lower():
            return (4.536 * weight) + (15.88 * height) - (5 * age) + 5
        elif "female" in sex.lower():
            return (4.536 * weight) + (15.88 * height) - (5 * age) - 161
    else:
        if "male" in sex.lower():
            return (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif "female" in sex.lower():
            return (10 * weight) + (6.25 * height) - (5 * age) - 161

# Calculates the user's TDEE, factoring in levels of activity, defined in dictionary activityLevels
def TDEE(BMR, activity, levels):
    return BMR * levels[activity]

# Calculates the user's caloric intake goal depending on what their diet goals are
def DIET(TDEE, diet):
    factor = (10 + diet) / 10
    return TDEE * factor

# Calculates the user's suggested protein intake depending on what their overall fitness goals are
# Factors are acquired through scientific research and simplifying ranges to mean values.
def PROTEIN(imperial, weight, goal):
    if (imperial):
        if goal == 1:
            return 0.91 * weight
        elif goal == 2:
            return 0.77 * weight
        elif goal == 3:
            return 0.454545 * weight
    else:
        if goal == 1:
            return 2 * weight
        elif goal == 2:
            return 1.7 * weight
        elif goal == 3:
            return 1 * weight
        
        
print("Hello! Welcome to Ahmed's Diet Advising Program!")
while True: 
    while True:
        try:
            age = int(input("What is your age? "))
            if 65 >= age >= 18:
                break
            elif age > 116 or age < 2:
                print("Please enter a valid age.")
            else:
                print("Sorry! This program uses Mifflen St-Jeor equations, which are most effective in age ranges 18-65.")
        except ValueError:
            print("Please enter a valid integer for your age")
            
    while True:
        unit = input("To start, would you like Imperial or Metric as your unit of measurement? ")
        if "imperial" in unit.lower():
            imperial = True
            break
        elif "metric" in unit.lower():
            imperial = False
            break
        else:
            print("Invalid unit of measurement. 'metric or imperial'")
        
    
    if (imperial):
        while True: 
            try:
                weight = float(input("What is your weight in " + unit.lower() + " (lbs)? "))
                if weight > 0:
                    break
                else:
                    print("Please enter a valid weight.")
            except ValueError:
                print("Please enter a valid value for your weight (lbs)")
            
        while True: 
            try:
                height = float(input("What is your height in " + unit.lower() + " (in)? "))
                if height > 0:
                    break
                else:
                    print("Please enter a valid height.")
            except ValueError:
                print("Please enter a valid value for your height (in)")
            
    
    else:
        while True: 
            try:
                weight = float(input("What is your weight in " + unit.lower() + " (kg)? "))
                if weight > 0:
                    break
                else:
                    print("Please enter a valid weight.")
            except ValueError:
                print("Please enter a valid value for your weight (kg)")
        while True: 
            try:
                height = float(input("What is your height in " + unit.lower() + " (cm)? "))
                if height > 0:
                    break
                else:
                    print("Please enter a valid height.")
            except ValueError:
                print("Please enter a valid value for your height (cm)")
    

            
    while True:
        sex = input("Male or Female? ")
        if "male" in sex.lower():
            break
        elif "female" in sex.lower():
            break
        else:
            print("Please enter a valid answer.")
    
    while True:
        try: 
            activity = int(input("On a scale of 1-5, how often do you exercise weekly? (1: none, 2: light exercises 1-3 days, 3: moderate exercise 3-5 days, 4: heavy exercise 6-7 days, 5: intense & vigorous daily) "))
            if 1 <= activity <= 5:
                break
            else:
                print("Please enter a valid answer. (1 to 5)")
        except ValueError:
            print("Please enter a valid answer. (1 to 5)")
    
    while True:
        try: 
            goal = int(input("What is your overall fitness goal? (1: fat loss/muscle maintain |  2: bulking/muscle building  | 3: none/weight loss focus) "))
            if 1 <= goal <= 3:
                break
            else:
                print("Please enter a valid answer. (1, 2, 3)")
        except ValueError:
            print("Please enter a valid answer. (1, 2, 3)")  
    
    while True:
        try: 
            diet = int(input("On a scale between -2 and 2, What are your dieting goals? (-2 being significant weight/fat loss and 2 being significant weight/muscle gain, 0 being none) "))
            if ((goal == 1 and diet < 0) or (goal == 2 and diet > 0) or (goal == 3 and diet <= 0)):        
                if -2 <= diet <= 2:
                    break
                else:
                    print("Please enter a valid answer (-2 to 2).")
            else:
                print("Please select an option that aligns with your goals.")
        except ValueError:
            print("Please enter a valid answer. (-2 to 2)")      

            


        

    print("------------------------------------------------------------------")
    myBMI = BMI(imperial, weight, height)
    myBMR = BMR(imperial, weight, height, sex, age)
    myProtein = PROTEIN(imperial, weight, goal)
    calIntake = TDEE(myBMR, activity, activityLevels)
    myDiet = (DIET(calIntake, diet))
    
    if  myBMI < 16:
        print("Your BMI (Body Mass Index) is: " + str(round(myBMI, 2)) + ". Watch out, you are severely underweight!")
    elif myBMI < 18.5: 
        print("Your BMI (Body Mass Index) is: " + str(round(myBMI, 2)) + ". Slightly underweight, almost there!")
    elif myBMI < 25:
        print("Your BMI (Body Mass Index) is: " + str(round(myBMI, 2)) + ". Healthy!")
    elif myBMI < 30:
        print("Your BMI (Body Mass Index) is: " + str(round(myBMI, 2)) + ". Slightly overweight, almost there!")
    elif myBMI >= 30:
        print("Your BMI (Body Mass Index) is: " + str(round(myBMI, 2)) + ". Watch out, you are severely overweight!")
        
    print(" ")
    print("Your BMR (Basal Metabolic Rate) is: " + str(round(myBMR)) + ".")
    print(" ")
    print("Your caloric maintenance is " + str(round(calIntake)) + ".")
    print(" ")
    print("Your suggested daily caloric intake for your diet is: " + (str(round(myDiet))) + ".")
    print(" ")
    print("Your suggested daily protein intake for your diet is: " + (str(round(myProtein, 2))) + ".")
    print("------------------------------------------------------------------")
    retry = str(input("Would you like to try again? (yes | no) "))
    if "no" in retry.lower() or "n" in retry.lower():
        print("Thank you for using Ahmed's Advising Program.")
        break
        
