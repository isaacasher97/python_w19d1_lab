# 1. Reverse String

# JS - 
# function reverseString(str){
#     return str.split("").reverse().join("")
# }

# console.log(reverseString("Hello World")) // "dlroW olleH"

# Python:

def reverse_string(s):
    return ''.join(reversed(s))

print(reverse_string("Hello World"))  # Output: "dlroW olleH"



# 2. Fizz Buzz

# JS -
# function fizzBuzz(num){
#     for (let index = 0; index < num; num++){
        
#         let result = ""

#         if (index % 3 === 0){
#             result = result + "fizz"
#         }

#         if (index % 5 === 0){
#             result = result + "buzz"
#         }

#         console.log(`${index} = `, result)
#     }
# }

# fizzBuzz(16)
# // 0 = "fizz buzz"
# // 1 = ""
# // 2 = ""
# // 3 = "fizz"
# // 4 = ""
# // 5 = "buzz"
# // 6 = "fizz"
# // 7 = ""
# // 8 = ""
# // 9 = "fizz"
# // 10 = "buzz"
# // 11 = ""
# // 12 = "fizz"
# // 13 = ""
# // 14 = ""
# // 15 = "fizzbuzz"


# Python:

def fizz_buzz(num):
    ## the range() function below is used on python to generate a sequence of numbers withing a specified range.
    for i in range(num): 
        result = ""

        if i % 3 == 0:
            result += "fizz "
        
        if i % 5 == 0:
            result += "buzz"
        
        print(f"{i} = {result}")
        
fizz_buzz(16)

# 3. Calculator

# JS - 
# function calculator(num1, num2, operation){
#     if (operations = "+"){
#         return num1 + num2
#     }
#     if (operations = "-"){
#         return num1 - num2
#     }
#     if (operations = "*"){
#         return num1 * num2
#     }
#     if (operations = "/"){
#         return num2 !== 0 ? num1/num2 : "Can't Divide by 0"
#     }
# }

# calculator(2,2,"+") //4


# Python:

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2 if num2 != 0 else "Can't Divide by 0" 
        # "if" acts as ? would in a js turnary statement. "else" also replaces ":" in turnary statements

result = calculator(2, 2, "+")
print(result)  # Output: 4

# 4. Random Number

# JS - 
# function randomNumber(low, max){
#     while (true){
#         const randomNum = Math.floor(Math.random() * max)

#         if(randomNum >= low && randomNum <= max){
#             return randomNum
#         }
#     }
# }

# console.log(randomNumber(10,20)) //random number between 10 and 20


# Python:

import random

def random_number(low, high):
    while True:
        random_num = random.randint(low, high)

        if low <= random_num <= high:
            return random_num
        
result = random_number(10, 20)
print(result) #output: random number between 10 and 20

##Both random.randint(low, high) in Python and Math.floor(Math.random() * max) in JavaScript are used to generate random numbers within a specified range. 

# In python, The random.randint() function in Python is part of the random module which was imported (used instead of Math.random). It directly generates a random integer between low and high instead of low to max. 

# The Python random.randint(low, high) function directly generates an integer within the specified range, which makes it more intuitive and easier to use when you want an integer result.

# In Python's random.randint(low, high), the range is inclusive of both low and high. This means that the random number generated can be equal to either low or high, While In JavaScript's Math.floor(Math.random() * max), the range includes 0 but excludes max. This means the random number generated will be in the range [0, max) – that is, greater than or equal to 0 and strictly less than max.