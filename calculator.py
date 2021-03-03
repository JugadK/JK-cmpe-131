

def input_output():
    """
    This function prompts the user to input 3 variables, number1,number2,operator. These operators and then inputed into the calculator function

    Returns
    -------
    boolean
        it returns True if the user enters n when prompted if they wan't to continue the program
    
    Examples
    --------
    >>input_output()
    False

    """
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")
    operator = input("Enter the operation: ")
    print(calculator(number1,number2,operator))
    exitChoice = input("\nDo you wish to exit? ")
    if(exitChoice == "n"):
        return True
    else:
        return False

def calculator(number1,number2,operator):
    """
    Calculator function that takes two numbers and applies one of 6 different operators, depending on what the user picked in input_output()

    The function checks if the number1 and number2 are both infact floats, then also checks if the string for operator is indeed a valid operator for the program
    it will then check for the right operator and then apply it to the numbers
    
    Parameters
    -----------
    number1 : float
        First Number
    number2 : float
        Second Number
    operator : String
        A string that contains the operator the user desires
    
    Returns
    -------
    float
        The solution for when the two numbers have the operator applied to them (Ex. 2*2=4)
    boolean
        returns False when a input is not valid

    Examples
    --------
    calculator(2,2,+)
    4.0
    calculator(2,2,*)
    4.0
    calculator(8,4,/)
    2.0

    """
    #all valid operators
    array = ['+','-','*','/','//','**']
    validOperator = False
    
    try:
        number1 = float(number1)
    except ValueError as e:
        return False
    try:
        number2 = float(number2)
    except ValueError as e:
        return False

        #This checks whether or not the operator is valid 
    for i in array:
        if(i == operator):
            validOperator = True
        #If the operator is not valid it just returns false
    if(validOperator == False):
        return False
    if(operator == '+'):
        return number1 + number2
    if(operator == '-'):
        return number1 - number2
    if(operator == '*'):
        return number1*number2
    if(operator == '/'):
        return number1 / number2
    if(operator == '//'):
        return number1//number2
    if(operator == '**'):
        return number1**number2
    
continue_calculator = True
while(continue_calculator == True):
    if(input_output() == False):
        continue_calculator = False


    

   
