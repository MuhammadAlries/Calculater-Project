import math 
print("Hello. it's calculater project with python ")

first_number = int(input("Please insert your first number  "))
operation = input ('please insert your operation : "+" ,  "-" , "*" , "/" , "pow" , "sqrt"  ')
print ("If you choose the 'sqrt' operation please don't fill in the second number  ")
second_number = int(input("Please insert your second number  "))


if (operation == "+") :
    result = first_number + second_number
    print( result)

elif (operation == "-") :
    result = first_number - second_number
    print(result)

elif (operation == "*") :
    result = first_number * second_number
    print( result)

elif (operation == "/" ) :
    result = first_number / second_number
    print(result)

elif (operation == "pow") :
    result = math.pow(first_number,second_number)
    print( result)

elif (operation == "sqrt" and "root") :
    result = math.sqrt(first_number)
    print( result)

else :
    print ("We don't supported this operation . You can use the '+' ,  '-' , '*' , '/' , 'pow' , 'sqrt'")


 


