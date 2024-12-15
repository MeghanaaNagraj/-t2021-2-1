class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "addition":
            return f"Result: {self.add()}"
        elif self.operation == "subtraction":
            return f"Result: {self.subtract()}"
        elif self.operation == "multiplication":
            return f"Result: {self.multiply()}"
        elif self.operation == "division":
            return self.divide()
        else:
            return "Invalid operation. Please choose from Addition, Subtraction, Multiplication, or Division."

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed."
        return f"Result: {self.a / self.b}"

if __name__ == "__main__":
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        operation = input("Enter the type of operation (Addition, Subtraction, Multiplication, Division): ")

        calc = Calculator(a, b, operation)
        result = calc.calculate()
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values for 'a' and 'b'.")
