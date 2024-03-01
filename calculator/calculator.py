class Calculator:
    commands = {
        'add': 'Addition',
        'subtract': 'Subtraction',
        'multiply': 'Multiplication',
        'divide': 'Division',
        'menu': 'Display Menu',
    }

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @classmethod
    def display_menu(cls):
        print("Available Commands:")
        for command, description in cls.commands.items():
            print(f"{command}: {description}")

if __name__ == "__main__":
    Calculator.display_menu()

