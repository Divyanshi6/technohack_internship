#""""""""""""""""""""""""""""""""""""""""""""""""  CALCULATOR  """"""""""""""""""""""""""""""""""""""""""""""""


def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def power(n1,n2):
    return pow(n1,n2)

print("Select the arithmetic operation you want to perform")
print("(1)Add")
print("(2)Subtract")
print("(3)Multiply")
print("(4)Divide")
print("(5)Powe or exponentiation")

while True:
    choice = input("Enter choice(1 or 2 or 3 or 4 or 5): ")

    if choice in ('1', '2', '3', '4','5'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("[Addition]",n1, "+", n2, "=", add(n1, n2))

        elif choice == '2':
            print("[Subtraction]",n1, "-", n2, "=", subtract(n1, n2))

        elif choice == '3':
            print("[Multiplication]",n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '4':
            print("[Division]",n1, "/", n2, "=", divide(n1, n2))

        elif choice == '5':
            print("[Power]",n1, " ^ ", n2, "=", power(n1, n2))    
        
        next_calculation = input("Want to do next calculation? (yes or no): ")
        if next_calculation == "no" or "No" or "NO":
          print("Calculation completed:>")
          break
    else:
        print("Sorry!,Invalid Choice...please choose from the given choices")