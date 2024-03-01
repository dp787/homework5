class Calculator:
    commands = {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b if b != 0 else None,
    }
    
    @staticmethod
    def execute_command(command: str, a: float, b: float) -> float:
        if command in Calculator.commands:
            return Calculator.commands[command](a, b)
        else:
            raise ValueError(f"Invalid command: {command}")

    @staticmethod
    def print_menu():
        print("Available Commands:")
        for cmd in Calculator.commands:
            print(f"- {cmd}")

# REPL loop
while True:
    user_input = input("Enter command (type 'exit' to quit): ").lower()

    if user_input == 'exit':
        break

    if user_input == 'menu':
        Calculator.print_menu()
        continue

    try:
        command, a, b = user_input.split()
        a, b = float(a), float(b)
        result = Calculator.execute_command(command, a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
