#====================== PYTHON FUNCTIONS ASSIGNMENT ======================

# 1. Create a simple function called greet() that returns "Hello World".
# Answer no 1 here.
def greet():
          
   return "Hello World"


# print(greet())


# 2. Create a function called add_numbers() that adds two numbers (5 and 10)
#   inside the function and returns the result.
# Answer no 2 here.

def add_numbers():
    
    num1 = 5
    num2 = 10
    return num1 + num2
#print(add_numbers())

# 3. Create a function called introduction() that returns your name and age in a sentence.
#    Example: "My name is King and I am 25 years old."
# Answer no 3 here.

def introduction():
     age = 25
     return f"my name is Tivsue and i am {age} years old."
#print(introduction())


# 4. Create a function called area_of_square() that takes one parameter (side)
#    and returns the area of a square (side * side).
# Answer no 4 here.

def area_of_square(side):
    return side * side
side_length = 5
area = area_of_square (side_length)
print(f"The area of a square with side length {side_length} is: {area}")

# 5. Create a function called multiply_numbers(num1, num2)
#    that returns the product of the two numbers.
#    Call the function three times with different values and print the results.

# Answer no 5 here.
def multiply_numbers(num1, num2): 
  return num1 * num2

# Call the function three times with different values and print the results
result1 = multiply_numbers(5, 3)
print(f"The product of 5 and 3 is: {result1}")

result2 = multiply_numbers(10, -2)
print(f"The product of 10 and -2 is: {result2}")

result3 = multiply_numbers(7, 4)
print(f"The product of 7.5 and 4 is: {result3}")

# 6. Create a function that returns True if a number is greater than 10, otherwise returns False.
#    (You can name it check_number)
# Answer no 6 here.

def check_number():
     if 5 > 20:
         return print(True)
     else:
         print(False)       
print(check_number())

# 7. Demonstrate the difference between a global variable and a local variable
#    inside a function. Use print() to show both.
# Answer no 7 here.




# 8. Create a function called describe_pet(animal, name)
#    that returns a sentence like "My pet dog is named Rocky."
#    Call it using keyword arguments.
# Answer no 8 here.

def describe_pet(animal, name):
  return f"My pet {animal} is named {name}."

print(describe_pet(animal="dog", name="Rocky"))

# 9. Create a function called favorite_colors(*colors)
#    that accepts any number of colors and returns them as a tuple.
# Answer no 9 here.
def  favorite_colors(colors):
        return colors

result = favorite_colors = ('black', 'red', 'white')
print(f"favorite_colors:{result}")


# 10. Create a function called student_profile(**data)
#     that accepts any number of keyword arguments (name, age, grade, etc.)
#     and returns them as a dictionary.
# Answer no 10 here.

def student_profile(data):
    return data 
datas = student_profile = {
    'name': 'taver',
     'age': 25,
     'level': 200
    }
print(f"dictionary:",[datas])