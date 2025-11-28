def SmartCalculator():
    try:
        operation = input("Choose the operation that you want to perform: (+, -, /, *) ") 
        num_1= int(input("Enter the first number: "))
        num_2= int(input("Enter the second number: "))
    except ValueError:
        print("Invalid Input!! This program only works with numbers")
        return

    if operation=='+':
        result = num_1+ num_2
        print(f"{num_1} + {num_2} = {result}")
        
    elif operation=='-':
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")
        
    elif operation == '/':
        if num_2 == 0: 
             print("Invalid division! Division by 0 isnt allowed!")
        else: 
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}")
           
    elif operation=='*':
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")
    else:
        print("Invalid operation! Please choose from (+, -, /, *).")

#Calling the function to use it
SmartCalculator()
      
            
