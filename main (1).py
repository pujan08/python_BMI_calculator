# BMI calculator 
height = input("enter your height in cm:")
weight = input("enter your weight in kg:")

weight=int(weight)
height=float(height)
height=height/100
bmi=weight/(height*height)
answer=str(int(bmi))
print("Your BMI is "+answer)
