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