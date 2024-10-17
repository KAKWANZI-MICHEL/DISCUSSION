# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
def classify_temperature(temperature):

  if temperature < 0:
    return "Freezing"
  elif temperature <= 10:
    return "Cold"
  elif temperature <= 20:
    return "Moderate"
  elif temperature <= 30:
    return "Warm"
  else:
    return "Hot"

# temperature of the user
temperature = float(input("Enter the temperature: "))
result = classify_temperature(temperature)
print("The temperature is:", result)


# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
import math

def calculate_sphere_volume(radius):

  volume = (4/3) * math.pi * radius ** 3
  return volume
radius = float(input("Enter the radius of the sphere: "))

volume = calculate_sphere_volume(radius)
print("The volume of the sphere is:", round(volume, 1))