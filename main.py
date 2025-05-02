#lesson 9
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")

    #Lesson 10
    # prompt: generate a comprehensive example of file handling using all the functions

# Create a file and write to it
with open('example.txt', 'w') as f:
  f.write("This is line 1.\n")
  f.write("This is line 2.\n")
  f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read the file and print its content
with open('example.txt', 'r') as f:
  content = f.read()
  print("--- Full Content ---")
  print(content)

# Read the file line by line and print each line
with open('example.txt', 'r') as f:
  print("--- Line by Line ---")
  for line in f:
    print(line, end='')

# Read a single line
with open('example.txt', 'r') as f:
  print("\n--- Readline ---")
  print(f.readline(), end='')

  # Read all lines into a list
with open('example.txt', 'r') as f:
  lines = f.readlines()
  print("\n--- Readlines ---")
  for line in lines:
    print(line, end='')

# Append to the file
with open('example.txt', 'a') as f:
  f.write("This is appended line 1.\n")
  f.write("This is appended line 2.\n")

# Reading with seek and tell
with open('example.txt', 'r') as f:
  print("\n--- Seek and Tell ---")
  print("Current position:", f.tell())
  print("First line:", f.readline(), end="")
  print("Current position:", f.tell())
  f.seek(0)
  print("After seek(0):", f.tell())
  print("First line again:", f.readline(), end="")

# Demonstrating 'x' mode (exclusive creation)
try:
    with open('new_file.txt', 'x') as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")

    # Copy file example
def copy_file(source, destination):
  try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
      for line in src:
        dest.write(line)
      print(f"'{source}' successfully copied to '{destination}'")
  except FileNotFoundError:
    print(f"Error: File not found '{source}'")
  except Exception as e:
    print(f"Error during copying: {e}")

copy_file("example.txt", "example_copy.txt")

#lesson 11import math

# abs() returns the absolute value of a number
# In Python, abs() is a built-in function, which means it's a global function
# available in the standard library without needing to import any specific modules.
# You can use it directly in your code.
print("abs(-5) = ", abs(-5))  # outputs: 5

# pow() raises a number to a power
print("pow(2, 3) = ", pow(2, 3))  # outputs: 8

# round() rounds a number to a specified number of decimal places
print("round(3.14159, 2) = ", round(3.14159, 2))  # outputs: 3.14

# max() returns the largest of a set of numbers
print("max(1, 2, 3, 4, 5) = ", max(1, 2, 3, 4, 5))  # outputs: 5

# min() returns the smallest of a set of numbers
print("min(1, 2, 3, 4, 5) = ", min(1, 2, 3, 4, 5))  # outputs: 1

# math.sin() returns the sine of an angle in radians
print("math.sin(math.pi/2) = ", math.sin(math.pi/2))  # outputs: 1.0

# math.cos() returns the cosine of an angle in radians
print("math.cos(0) = ", math.cos(0))  # outputs: 1.0

# math.tan() returns the tangent of an angle in radians
print("math.tan(math.pi/4) = ", math.tan(math.pi/4))  # outputs: 1.0

# math.sqrt() returns the square root of a number
print("math.sqrt(9) = ", math.sqrt(9))  # outputs: 3.0

# math.factorial() returns the factorial of a number
print("math.factorial(5) = ", math.factorial(5))  # outputs: 120

# math.log() returns the natural logarithm of a number
print("math.log(10) = ", math.log(10))  # outputs: 2.302585092994046

# math.log10() returns the base-10 logarithm of a number
print("math.log10(100) = ", math.log10(100))  # outputs: 2.0

# math.exp() returns the value of e raised to a power
print("math.exp(2) = ", math.exp(2))  # outputs: 7.38905609893065

# math.ceil() returns the smallest integer greater than or equal to a number
print("math.ceil(4.7) = ", math.ceil(4.7))  # outputs: 5

# math.floor() returns the largest integer less than or equal to a number
print("math.floor(4.7) = ", math.floor(4.7))  # outputs: 4

# math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("math.pi = ", math.pi)  # outputs: 3.14159265359

# math.e is a constant representing the base of the natural logarithm
print("math.e = ", math.e)  # outputs: 2.718281828459045

# math.tau is a constant representing the ratio of a circle's circumference to its radius
print("math.tau = ", math.tau)  # outputs: 6.283185307179586

# math.inf is a constant representing infinity
print("math.inf = ", math.inf)  # outputs: inf

# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan)  # outputs: nan
