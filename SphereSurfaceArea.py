import math

# Ask the user for the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the surface area of the sphere
surface_area = 4 * math.pi * (radius**2)

# Display the surface area
print(f"The surface area of the sphere with radius {radius} is: {surface_area:.2f}")
