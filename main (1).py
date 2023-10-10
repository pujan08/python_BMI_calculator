# BMI calculator 
height = input("enter your height in cm:")
weight = input("enter your weight in kg:")

a=int(weight)
b=float(height)
b=b/100
bmi=a/(b*b)
answer=str(int(bmi))
print("Your BMI is "+answer)
