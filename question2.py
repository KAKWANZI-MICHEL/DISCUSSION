# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calculate_bmi(weight, height):


  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal weight"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

weight = float(input("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height) 

bmi_category = calculate_bmi(bmi)
print("Your BMI is:", bmi)
print("Your BMI category is:", bmi_category)




# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

import math

def calculate_cylinder_volume(radius, height):

  volume = math.pi * radius ** 2 * height
  return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = calculate_cylinder_volume(radius, height)

print("The volume of the cylinder is:", volume)