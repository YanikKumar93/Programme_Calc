print("****** CALCULATOR ******")
def find_valid_number():
    input_value = input("What is the Value ?: ")
    if input_value.isdigit():
        return (int(input_value))
    elif input_value.replace(".", "1").isdigit() and len(input_value.split(".")) == 2:
        return (float(input_value))
    else:
        print("Please enter a valid value.")
        return "INVALID"
def Add():
    Value = 0
    AVALUE = input("How many numbers to add ?: ")
    Counter = 0
    if AVALUE.isdigit():
        Success = int(AVALUE)
        while Counter < Success:
            Val = find_valid_number()
            if Val == "INVALID":
                print(Val)
            else:
                Value += Val
                Counter += 1
            if Counter == Success:
                print(Value)
    else:
        print("Please enter a valid number")
def Sub():
    Value = 0
    Counter = 0
    while Counter < 1:
        Val = find_valid_number()
        if Val == "INVALID":
            print(Val)
        else:
            Value += Val
            Counter += 1
    while Counter < 2:
        Num2I = find_valid_number()
        if Num2I == "INVALID":
            print(Num2I)
        else:
            Value -= Num2I
            Counter += 1
        if Counter == 2:
            print(Value)

def Mul():
    Mvalue = input("How many numbers to multiply ?: ")
    Result = 1
    Counter = 0
    if Mvalue.isdigit():
        Success1 = int(Mvalue)
        while Counter < Success1:
            Val = find_valid_number()
            if Val == "INVALID":
                print(Val)
            else:
                Result *= Val
                Counter += 1
            if Success1 == Counter:
                print(Result)
    else:
        print("Please enter a valid number.")
def Div():
    Valuee = 0
    Counter = 0
    while Counter < 1:
        print("Enter Dividend : ")
        Dividend = find_valid_number()
        if Dividend == "INVALID":
            print(Dividend)
        else:
            Valuee += Dividend
            Counter += 1
    while Counter < 2:
        print("Enter Divisor : ")
        Divisor = find_valid_number()
        if Divisor == "INVALID":
            print(Divisor)
        elif Divisor == 0:
            print("Division by zero is not valid. Please try again.")
        else:
            Valuee /= Divisor
            Counter += 1
    if Counter == 2:
        print(Valuee)
def Expo():
    Counter = 0
    Result = 0
    while Counter < 1:
        Valu = input("What is the Base Number ?: ")
        if Valu.isdigit():
            ValuI = int(Valu)
            Result += ValuI
            Counter += 1
        elif Valu.replace(".", "1").isdigit() and len(Valu.split(".")) == 2:
            ValuF = float(Valu)
            Result += ValuF
            Counter += 1
        else:
            print("Please enter a valid value.")
    while Counter < 2:
        Valy = input("What is the power ?: ")
        if Valy.isdigit():
            ValyI = int(Valy)
            Result **= ValyI
            Counter += 1
        elif Valy.replace(".", "1").isdigit() and len(Valy.split(".")) == 2:
            ValyF = float(Valy)
            Result **= ValyF
            Counter += 1
        else:
            print("Please enter a valid value.")
    if Counter == 2:
        print(Result)
def Sq():
    Counter = 0
    Resultt = 0
    while Counter < 1:
        Base = input("What is the number to be squared ?: ")
        if Base.isdigit():
            BasI = int(Base)
            Res = (BasI * BasI)
            Resultt += Res
            Counter += 1
        elif Base.replace(".", "1").isdigit() and len(Base.split(".")) == 2:
            BasF = float(Base)
            Res = (BasF * BasF)
            Resultt += Res
            Counter += 1
    if Counter == 1:
        print(Resultt)

def Ter():
    print("\n The Calculator is hereby being terminated.\n Thank You.\n This is created by Yanik Kumar ")

while True:
    print("**************")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION ")
    print("5. EXPONENTIATION")
    print("6. SQUARE")
    print("7. TERMINATE")
    print("********** Please write the number accompanied along the function *********")
    command = input("Please write your choice from 1 to 7 : ")
    if command.isdigit():
        command = int(command)
        if command == 1:
            Add()
        elif command == 2:
            Sub()
        elif command == 3:
            Mul()
        elif command == 4:
            Div()
        elif command == 5:
            Expo()
        elif command == 6:
            Sq()
        elif command == 7:
            Ter()
            break
    else:
        print("Please enter a a valid value.")
