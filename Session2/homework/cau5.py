x = int(input("Ban cao bao nhieu cm? ")) / 100
y = int(input("Ban nang bao nhieu kg? "))

BMI = y / x**2

if BMI < 16:
    print ("Severely")
elif BMI < 18.5:
    print ("Underweight")
elif BMI < 25:
    print ("Normal")
elif BMI < 30:
    print ("Overweight")
else:
    print ("Obese")
