class Calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Cannot divide by 0"
        return x * 1.0 / y

    def calculate_sum(n):
        # Code complexity
        result = 0
        for i in range(n):
            result += i * i + 1

        # Duplication
        total_sum = result + result

        # Unused variable
        unused_var = 10

        return total_sum
