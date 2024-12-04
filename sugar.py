try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform addition and subtraction
    sum_result = num1 + num2
    subtract_result = num1 - num2
    
    # Display the results
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference between {num1} and {num2} is: {subtract_result}")
except ValueError:
    print("Please enter valid numbers!") 